#!/usr/bin/env python3
"""
Download and steal existing commands from GitHub repositories.

This script copies valid commands (.md files) from GitHub repos.
It does NOT convert arbitrary files into commands.

Usage:
    steal_to_command.py <username/repo> --path <command.md> [--dest <destination>]
    steal_to_command.py <github-url> --path <command.md> [--dest <destination>]

Examples:
    steal_to_command.py user/repo --path command/check-code.md
    steal_to_command.py user/repo --path commands/my-command.md
    steal_to_command.py https://github.com/user/repo --path some-script.md
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


def find_all_commands(repo_dir: Path) -> list[tuple[Path, str]]:
    """
    Find all .md command files in the repository.
    
    Returns:
        List of tuples: (command_file_path, relative_path_string)
    """
    commands = []
    
    # Common command directory patterns to search
    search_patterns = [
        "commands/*.md",             # Claude Code / Codex style: commands/
        "command/*.md",              # OpenCode style: command/
        ".claude/commands/*.md",     # Claude Code repo-specific
        ".codex/commands/*.md",      # Codex repo-specific
        ".opencode/command/*.md",    # OpenCode repo-specific
        "*.md",                      # Root level .md files
    ]
    
    found_paths = set()  # Avoid duplicates
    
    for pattern in search_patterns:
        for cmd_file in repo_dir.glob(pattern):
            if cmd_file.is_file():
                rel_path = cmd_file.relative_to(repo_dir)
                path_key = str(rel_path)
                
                if path_key not in found_paths:
                    found_paths.add(path_key)
                    commands.append((cmd_file, str(rel_path)))
    
    return sorted(commands, key=lambda x: x[1])


def suggest_commands(repo_dir: Path, attempted_path: str) -> str:
    """Create helpful error message with available commands."""
    commands = find_all_commands(repo_dir)
    
    if not commands:
        msg = "❌ No .md command files found in this repository.\n\n"
        msg += "Commands must be .md files.\n"
        msg += "Check if you're pointing to the correct repository."
        return msg
    
    msg = f"❌ Path '{attempted_path}' does not point to a valid .md command file.\n\n"
    
    msg += f"Found {len(commands)} command(s) in this repository:\n"
    for _, rel_path in commands:
        msg += f"  - {rel_path}\n"
    
    msg += "\n💡 Try one of these:\n"
    for _, rel_path in commands[:3]:  # Show max 3 examples
        msg += f"  python3 steal_to_command.py <repo> --path {rel_path}\n"
    
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


def steal_command(repo_dir: Path, subpath: str | None, dest_dir: Path, command_name: str | None = None) -> Path | None:
    """
    Steal an existing command (.md file) from a downloaded repo.
    
    Args:
        repo_dir: Root directory of the downloaded repo
        subpath: Subpath within the repo to the command file
        dest_dir: Destination directory for commands
        command_name: Optional custom name for the command
    
    Returns:
        Path to the copied command file, or None if cancelled
    
    Raises:
        Exception: If path is not provided or doesn't point to a .md file
    """
    if not subpath:
        raise Exception("--path is required for commands (specify the .md file to steal)")
    
    source_path = repo_dir / subpath
    if not source_path.exists():
        raise Exception(f"Path '{subpath}' not found in repository")
    
    print(f"📂 Source: {source_path}")
    
    # Validate it's a .md file
    if not source_path.is_file() or source_path.suffix != '.md':
        # Not a valid command - provide helpful suggestions
        error_msg = suggest_commands(repo_dir, subpath)
        raise Exception(error_msg)
    
    print(f"✅ Found .md file - stealing command")
    
    # Determine command name
    if command_name is None:
        command_name = source_path.stem  # Remove extension
    
    # Sanitize command name
    command_name = re.sub(r'[^a-z0-9-]', '-', command_name.lower()).strip('-')
    
    command_dest = dest_dir / f"{command_name}.md"
    
    if command_dest.exists():
        print(f"⚠️  Command '{command_name}' already exists at {command_dest}")
        response = input("   Overwrite? [y/N]: ").strip().lower()
        if response != 'y':
            print("❌ Cancelled")
            return None
    
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy the .md file
    shutil.copy2(source_path, command_dest)
    print(f"✅ Command copied to: {command_dest}")
    return command_dest


def main():
    parser = argparse.ArgumentParser(
        description="Steal an existing command from a GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  steal_to_command.py user/repo --path command/check-code.md
  steal_to_command.py user/repo --path commands/my-command.md
  steal_to_command.py https://github.com/user/repo --path script.md
        """
    )
    
    parser.add_argument("repo", help="GitHub repository (username/repo or full URL)")
    parser.add_argument("--path", required=True, help="Path to the command file/directory in the repo")
    parser.add_argument("--dest", help="Destination directory (default: ./command/)")
    parser.add_argument("--name", help="Custom name for the command")
    
    args = parser.parse_args()
    
    try:
        username, repo = parse_github_input(args.repo)
        repo_dir = download_github_repo(username, repo)
        
        dest_dir = Path(args.dest).resolve() if args.dest else Path.cwd() / "command"
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        result = steal_command(repo_dir, args.path, dest_dir, args.name)
        
        if result:
            print(f"\n✨ Success! Command ready at: {result}")
            return 0
        else:
            return 1
    
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
