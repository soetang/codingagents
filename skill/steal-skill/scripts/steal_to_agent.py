#!/usr/bin/env python3
"""
Download and steal existing agents from GitHub repositories.

This script copies valid agents (.md files) from GitHub repos.
It does NOT convert arbitrary files into agents.

Usage:
    steal_to_agent.py <username/repo> --path <agent.md> [--dest <destination>]
    steal_to_agent.py <github-url> --path <agent.md> [--dest <destination>]

Examples:
    steal_to_agent.py user/repo --path agent/code-reviewer.md
    steal_to_agent.py user/repo --path agents/my-agent.md
    steal_to_agent.py https://github.com/user/repo --path some-agent.md
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
    """Parse various GitHub input formats into (username, repo)."""
    if input_str.startswith(("http://", "https://")):
        parsed = urlparse(input_str)
        if parsed.netloc not in ("github.com", "www.github.com"):
            raise ValueError(f"Only GitHub URLs are supported, got: {parsed.netloc}")
        path = parsed.path.lstrip("/").removesuffix(".git")
        parts = path.split("/")
        if len(parts) < 2:
            raise ValueError(f"Invalid GitHub URL format: {input_str}")
        return parts[0], parts[1]
    
    if "/" not in input_str:
        raise ValueError(f"Invalid format. Expected 'username/repo' or GitHub URL")
    
    parts = input_str.split("/", 1)
    return parts[0], parts[1]


def find_all_agents(repo_dir: Path) -> list[tuple[Path, str]]:
    """
    Find all .md agent files in the repository.
    
    Returns:
        List of tuples: (agent_file_path, relative_path_string)
    """
    agents = []
    
    # Common agent directory patterns to search
    search_patterns = [
        "agents/*.md",             # Claude Code / Codex style: agents/
        "agent/*.md",              # OpenCode style: agent/
        ".claude/agents/*.md",     # Claude Code repo-specific
        ".codex/agents/*.md",      # Codex repo-specific
        ".opencode/agent/*.md",    # OpenCode repo-specific
        "*.md",                    # Root level .md files
    ]
    
    found_paths = set()  # Avoid duplicates
    
    for pattern in search_patterns:
        for agent_file in repo_dir.glob(pattern):
            if agent_file.is_file():
                rel_path = agent_file.relative_to(repo_dir)
                path_key = str(rel_path)
                
                if path_key not in found_paths:
                    found_paths.add(path_key)
                    agents.append((agent_file, str(rel_path)))
    
    return sorted(agents, key=lambda x: x[1])


def suggest_agents(repo_dir: Path, attempted_path: str) -> str:
    """Create helpful error message with available agents."""
    agents = find_all_agents(repo_dir)
    
    if not agents:
        msg = "❌ No .md agent files found in this repository.\n\n"
        msg += "Agents must be .md files.\n"
        msg += "Check if you're pointing to the correct repository."
        return msg
    
    msg = f"❌ Path '{attempted_path}' does not point to a valid .md agent file.\n\n"
    
    msg += f"Found {len(agents)} agent(s) in this repository:\n"
    for _, rel_path in agents:
        msg += f"  - {rel_path}\n"
    
    msg += "\n💡 Try one of these:\n"
    for _, rel_path in agents[:3]:  # Show max 3 examples
        msg += f"  python3 steal_to_agent.py <repo> --path {rel_path}\n"
    
    return msg


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
                if branch == "main":
                    print("   Branch 'main' not found, trying 'master'...")
                    return download_github_repo(username, repo, "master")
                else:
                    raise Exception(f"Repository '{username}/{repo}' not found on GitHub")
            
            response.raise_for_status()
            tarball_path.write_bytes(response.content)
    
    except httpx.HTTPStatusError as e:
        raise Exception(f"Failed to download repository: {e}")
    except httpx.RequestError as e:
        raise Exception(f"Network error: {e}")
    
    extract_path = tmp_dir / "extracted"
    print(f"📦 Extracting repository...")
    
    with tarfile.open(tarball_path, "r:gz") as tar:
        tar.extractall(extract_path)
    
    repo_dir = extract_path / f"{repo}-{branch}"
    if not repo_dir.exists():
        raise Exception(f"Unexpected tarball structure: expected {repo_dir}")
    
    return repo_dir


def steal_agent(repo_dir: Path, subpath: str | None, dest_dir: Path, agent_name: str | None = None) -> Path | None:
    """
    Steal an existing agent (.md file) from a downloaded repo.
    
    Args:
        repo_dir: Root directory of the downloaded repo
        subpath: Subpath within the repo to the agent file
        dest_dir: Destination directory for agents
        agent_name: Optional custom name for the agent
    
    Returns:
        Path to the copied agent file, or None if cancelled
    
    Raises:
        Exception: If path is not provided or doesn't point to a .md file
    """
    if not subpath:
        raise Exception("--path is required for agents (specify the .md file to steal)")
    
    source_path = repo_dir / subpath
    if not source_path.exists():
        raise Exception(f"Path '{subpath}' not found in repository")
    
    print(f"📂 Source: {source_path}")
    
    # Validate it's a .md file
    if not source_path.is_file() or source_path.suffix != '.md':
        # Not a valid agent - provide helpful suggestions
        error_msg = suggest_agents(repo_dir, subpath)
        raise Exception(error_msg)
    
    print(f"✅ Found .md file - stealing agent")
    
    # Determine agent name
    if agent_name is None:
        agent_name = source_path.stem  # Remove extension
    
    # Sanitize agent name
    agent_name = re.sub(r'[^a-z0-9-]', '-', agent_name.lower()).strip('-')
    
    agent_dest = dest_dir / f"{agent_name}.md"
    
    if agent_dest.exists():
        print(f"⚠️  Agent '{agent_name}' already exists at {agent_dest}")
        response = input("   Overwrite? [y/N]: ").strip().lower()
        if response != 'y':
            print("❌ Cancelled")
            return None
    
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy the .md file
    shutil.copy2(source_path, agent_dest)
    print(f"✅ Agent copied to: {agent_dest}")
    return agent_dest


def main():
    parser = argparse.ArgumentParser(
        description="Steal an existing agent from a GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  steal_to_agent.py user/repo --path agent/code-reviewer.md
  steal_to_agent.py user/repo --path agents/my-agent.md
  steal_to_agent.py https://github.com/user/repo --path agent.md
        """
    )
    
    parser.add_argument("repo", help="GitHub repository (username/repo or full URL)")
    parser.add_argument("--path", required=True, help="Path to the agent file/directory in the repo")
    parser.add_argument("--dest", help="Destination directory (default: ./agent/)")
    parser.add_argument("--name", help="Custom name for the agent")
    
    args = parser.parse_args()
    
    try:
        username, repo = parse_github_input(args.repo)
        repo_dir = download_github_repo(username, repo)
        
        dest_dir = Path(args.dest).resolve() if args.dest else Path.cwd() / "agent"
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        result = steal_agent(repo_dir, args.path, dest_dir, args.name)
        
        if result:
            print(f"\n✨ Success! Agent ready at: {result}")
            return 0
        else:
            return 1
    
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
