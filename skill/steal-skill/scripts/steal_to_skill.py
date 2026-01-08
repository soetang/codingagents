#!/usr/bin/env python3
"""
Download and steal existing skills from GitHub repositories.

This script copies valid skills (directories with SKILL.md) from GitHub repos.
It does NOT convert arbitrary repos into skills.

Usage:
    steal_to_skill.py <username/repo> [--path <subpath>] [--dest <destination>]
    steal_to_skill.py <github-url> [--path <subpath>] [--dest <destination>]

Examples:
    steal_to_skill.py anthropics/skills --path skills/analyze-paper
    steal_to_skill.py soetang/codingagents --path skill/hello-world
    steal_to_skill.py https://github.com/user/repo --path some/nested/skill
    steal_to_skill.py user/repo --dest ./my-custom-location
"""

import argparse
import re
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path
from urllib.parse import urlparse

try:
    import httpx
except ImportError:
    print("Error: httpx is required. Install with: pip install httpx")
    sys.exit(1)


def parse_github_input(input_str: str) -> tuple[str, str]:
    """
    Parse various GitHub input formats into (username, repo).
    
    Supports:
    - username/repo
    - https://github.com/username/repo
    - https://github.com/username/repo.git
    """
    # If it's a URL, parse it
    if input_str.startswith(("http://", "https://")):
        parsed = urlparse(input_str)
        if parsed.netloc not in ("github.com", "www.github.com"):
            raise ValueError(f"Only GitHub URLs are supported, got: {parsed.netloc}")
        
        # Remove leading slash and .git suffix
        path = parsed.path.lstrip("/").removesuffix(".git")
        parts = path.split("/")
        
        if len(parts) < 2:
            raise ValueError(f"Invalid GitHub URL format: {input_str}")
        
        return parts[0], parts[1]
    
    # Otherwise assume username/repo format
    if "/" not in input_str:
        raise ValueError(f"Invalid format. Expected 'username/repo' or GitHub URL, got: {input_str}")
    
    parts = input_str.split("/", 1)
    return parts[0], parts[1]


def download_github_repo(username: str, repo: str, branch: str = "main") -> Path:
    """Download a GitHub repository tarball and extract it."""
    tarball_url = f"https://github.com/{username}/{repo}/archive/refs/heads/{branch}.tar.gz"
    
    print(f"📥 Downloading {username}/{repo} from branch '{branch}'...")
    
    tmp_dir = Path(tempfile.mkdtemp())
    tarball_path = tmp_dir / "repo.tar.gz"
    
    try:
        with httpx.Client(follow_redirects=True, timeout=30.0) as client:
            response = client.get(tarball_url)
            
            if response.status_code == 404:
                # Try 'master' branch if 'main' failed
                if branch == "main":
                    print("   Branch 'main' not found, trying 'master'...")
                    return download_github_repo(username, repo, "master")
                else:
                    raise Exception(f"Repository '{username}/{repo}' not found on GitHub (tried 'main' and 'master' branches)")
            
            response.raise_for_status()
            tarball_path.write_bytes(response.content)
    
    except httpx.HTTPStatusError as e:
        raise Exception(f"Failed to download repository: {e}")
    except httpx.RequestError as e:
        raise Exception(f"Network error: {e}")
    
    # Extract
    extract_path = tmp_dir / "extracted"
    print(f"📦 Extracting repository...")
    
    with tarfile.open(tarball_path, "r:gz") as tar:
        tar.extractall(extract_path)
    
    # Find the extracted repo directory (GitHub tarballs extract to repo-branch/)
    repo_dir = extract_path / f"{repo}-{branch}"
    
    if not repo_dir.exists():
        raise Exception(f"Unexpected tarball structure: expected {repo_dir}")
    
    return repo_dir


def find_skill_md(search_dir: Path) -> Path | None:
    """Find SKILL.md file in the directory."""
    skill_md = search_dir / "SKILL.md"
    return skill_md if skill_md.exists() else None


def find_all_skills(repo_dir: Path) -> list[tuple[Path, str]]:
    """
    Find all SKILL.md files in the repository.
    
    Returns:
        List of tuples: (skill_directory, relative_path_string)
    """
    skills = []
    
    # Common skill directory patterns to search
    search_patterns = [
        "skills/*/SKILL.md",              # Claude Code / Codex style: skills/skill-name/SKILL.md
        "skill/*/SKILL.md",               # OpenCode style: skill/skill-name/SKILL.md
        ".claude/skills/*/SKILL.md",      # Claude Code repo-specific
        ".codex/skills/*/SKILL.md",       # Codex repo-specific
        ".opencode/skill/*/SKILL.md",     # OpenCode repo-specific
        "*/SKILL.md",                     # Direct subdirectories
        "SKILL.md",                       # Root level
    ]
    
    found_paths = set()  # Avoid duplicates
    
    for pattern in search_patterns:
        for skill_md in repo_dir.glob(pattern):
            skill_dir = skill_md.parent
            # Get relative path from repo root
            rel_path = skill_dir.relative_to(repo_dir)
            path_key = str(rel_path)
            
            if path_key not in found_paths:
                found_paths.add(path_key)
                skills.append((skill_dir, str(rel_path)))
    
    return sorted(skills, key=lambda x: x[1])


def suggest_skills(repo_dir: Path, attempted_path: str | None) -> str:
    """Create helpful error message with available skills."""
    skills = find_all_skills(repo_dir)
    
    if not skills:
        msg = "❌ No skills found in this repository.\n\n"
        msg += "A valid skill must have a SKILL.md file.\n"
        msg += "Check if you're pointing to the correct repository."
        return msg
    
    msg = "❌ No SKILL.md found"
    if attempted_path:
        msg += f" at path '{attempted_path}'"
    msg += "\n\n"
    
    msg += f"Found {len(skills)} skill(s) in this repository:\n"
    for _, rel_path in skills:
        msg += f"  - {rel_path}/\n"
    
    msg += "\n💡 Try one of these:\n"
    for _, rel_path in skills[:3]:  # Show max 3 examples
        msg += f"  python3 steal_to_skill.py <repo> --path {rel_path}\n"
    
    return msg


def steal_skill(repo_dir: Path, subpath: str | None, dest_dir: Path, skill_name: str | None = None) -> Path | None:
    """
    Steal an existing skill from a downloaded repo.
    
    Args:
        repo_dir: Root directory of the downloaded repo
        subpath: Optional subpath within the repo to use as source
        dest_dir: Destination directory for skills (e.g., ~/.config/opencode/skill)
        skill_name: Optional custom name for the skill
    
    Returns:
        Path to the copied skill directory, or None if cancelled
    
    Raises:
        Exception: If no SKILL.md found at the target path
    """
    # Determine source directory
    if subpath:
        source_dir = repo_dir / subpath
        if not source_dir.exists():
            raise Exception(f"Subpath '{subpath}' not found in repository")
    else:
        source_dir = repo_dir
    
    print(f"📂 Source directory: {source_dir}")
    
    # Check if it's a valid skill (has SKILL.md)
    skill_md = find_skill_md(source_dir)
    
    if not skill_md:
        # Not a valid skill - provide helpful suggestions
        error_msg = suggest_skills(repo_dir, subpath)
        raise Exception(error_msg)
    
    print(f"✅ Found SKILL.md - stealing skill")
    
    # Determine skill name
    if skill_name is None:
        # Use the last component of the path as skill name
        if subpath:
            skill_name = Path(subpath).name
        else:
            skill_name = source_dir.name
    
    # Sanitize skill name (convert to lowercase, replace invalid chars with hyphens)
    skill_name = re.sub(r'[^a-z0-9-]', '-', skill_name.lower()).strip('-')
    
    # Prepare destination
    skill_dest = dest_dir / skill_name
    
    if skill_dest.exists():
        print(f"⚠️  Skill '{skill_name}' already exists at {skill_dest}")
        response = input("   Overwrite? [y/N]: ").strip().lower()
        if response != 'y':
            print("❌ Cancelled")
            return None
        shutil.rmtree(skill_dest)
    
    # Copy the entire skill directory
    shutil.copytree(source_dir, skill_dest)
    print(f"✅ Skill copied to: {skill_dest}")
    return skill_dest


def main():
    parser = argparse.ArgumentParser(
        description="Steal an existing skill from a GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  steal_to_skill.py anthropics/skills --path skills/analyze-paper
  steal_to_skill.py soetang/codingagents --path skill/hello-world
  steal_to_skill.py https://github.com/user/repo --path skill/my-skill
  steal_to_skill.py user/repo --dest ./my-custom-skills
  steal_to_skill.py user/repo --path subdir --name my-custom-name
        """
    )
    
    parser.add_argument(
        "repo",
        help="GitHub repository (username/repo or full URL)"
    )
    
    parser.add_argument(
        "--path",
        help="Subpath within the repository to use as the skill source"
    )
    
    parser.add_argument(
        "--dest",
        help="Destination directory for the skill (default: current directory's skill/)"
    )
    
    parser.add_argument(
        "--name",
        help="Custom name for the skill (default: derived from path/repo)"
    )
    
    args = parser.parse_args()
    
    try:
        # Parse GitHub input
        username, repo = parse_github_input(args.repo)
        
        # Download repo
        repo_dir = download_github_repo(username, repo)
        
        # Determine destination
        if args.dest:
            dest_dir = Path(args.dest).resolve()
        else:
            # Default to ./skill/ in current directory
            dest_dir = Path.cwd() / "skill"
        
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Steal the skill
        result = steal_skill(repo_dir, args.path, dest_dir, args.name)
        
        if result:
            print(f"\n✨ Success! Skill ready at: {result}")
            print(f"\n📝 Next steps:")
            print(f"   1. Review and edit {result}/SKILL.md")
            print(f"   2. Test the skill with Claude Code")
            return 0
        else:
            return 1
    
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        return 1
    
    finally:
        # Cleanup is handled by tempfile.mkdtemp cleanup
        pass


if __name__ == "__main__":
    sys.exit(main())
