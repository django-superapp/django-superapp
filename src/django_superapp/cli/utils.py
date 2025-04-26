import os
import subprocess
import shutil

import sysrsync

import click


def clone_repo(repo_url, target_directory):
    click.echo("Forking the repository...")
    if not is_gh_installed():
        raise click.ClickException(
            "gh is not installed. Please install it before running this command using `brew install gh`."
        )
    result = subprocess.run(["gh", "repo", "fork", repo_url, "--clone", target_directory], capture_output=True, text=True)
    if result.returncode != 0:
        raise click.ClickException(f"Failed to fork repository. Error: {result.stderr}")


def create_pr(fork_directory):
    click.echo("Creating the PR...")
    if not is_gh_installed():
        raise click.ClickException(
            "gh is not installed. Please install it before running this command using `brew install gh`."
        )
    result = subprocess.run(["gh", "pr", "create", "--web", "--fill"], capture_output=True, text=True, cwd=fork_directory)
    if result.returncode != 0:
        raise click.ClickException(f"Failed to create PR. Error: {result.stderr}")


def sync_directories(src, dst, copier_configuration=None):
    """
    Syncs files from src to dst, ignoring files specified in the gitignore file
    and additional user-provided regex patterns. Removes files from dst that
    don't exist in src respecting gitignore_file and ignore_patterns.

    :param src: Source directory path
    :param dst: Destination directory path
    :param copier_configuration: Copier configuration
    """
    if not is_rsync_installed():
        raise click.ClickException(
            "rsync is not installed. Please install it before running this command."
        )

    options = [
        '-av',
        '--delete',
    ]
    copier_excludes = (
        copier_configuration.get('_exclude', []) if copier_configuration else []
    ) + (
        copier_configuration.get('rsync_exclude', []) if copier_configuration else []
    )
    copied_excluded_files = [
        c
        for c in copier_excludes
        if not c.startswith('!')
    ]
    copied_included_files = [
        c
        for c in copier_excludes
        if c.startswith('!')
    ]
    for c in copied_included_files:
        options.append(f"--include={c[1:]}")
    sysrsync.run(
        source=src,
        destination=dst,
        options=options,
        exclusions=[
                            ".DS_Store",
                            "venv",
                            "superapp_fork",
                            ".git",
                            ".copier-answers.yml",
                            "{{_copier_conf.answers_file}}.jinja",
                        ] + copied_excluded_files,
        verbose=True,
    )


def remove_directory_if_exists(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)



def is_gh_installed():
    try:
        result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def is_git_installed():
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def is_github_installed():
    try:
        result = subprocess.run(["github", "help"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def is_rsync_installed():
    try:
        result = subprocess.run(["rsync", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def display_git_diff():
    if not is_git_installed():
        raise click.ClickException("git is not installed. Please install it before running this command.")

    try:
        result = subprocess.run(["git", "--no-pager", "diff"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def open_repo_in_github(repo_directory):
    click.echo(f"Please review and commit the changes in the forked repository {repo_directory}")
    if is_github_installed():
        click.echo("Opening the repository in GitHub Desktop...")
        try:
            result = subprocess.run(["github", "open", repo_directory], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
