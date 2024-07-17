import os
import subprocess
import shutil

import sysrsync

import click


def clone_repo(repo_url, target_directory, fork_directory):
    click.echo("Forking the repository...")
    if not is_gh_installed():
        raise click.ClickException(
            "gh is not installed. Please install it before running this command using `brew install gh`."
        )
    add_to_gitignore(target_directory, 'superapp_fork')
    remove_directory_if_exists(fork_directory)

    result = subprocess.run(["gh", "repo", "fork", repo_url, "--clone", f'{target_directory}/superapp_fork'], capture_output=True, text=True)
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
    sysrsync.run(
        source=src,
        destination=dst,
        options=['-av', '--delete'],
        exclusions=[
                            ".DS_Store",
                            "superapp_fork",
                            ".git",
                            ".copier-answers.yml",
                            "{{_copier_conf.answers_file}}.jinja",
                        ] + copier_configuration.get('_exclude', []) if copier_configuration else [],
        verbose=True,

    )


def remove_directory_if_exists(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)



def add_to_gitignore(target_directory, entry):
    gitignore_path = os.path.join(target_directory, '.gitignore')

    # Check if .gitignore file exists
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            lines = file.readlines()

        # Check if entry already exists
        if not(entry + '\n' in lines or entry in lines):
            with open(gitignore_path, 'a') as file:
                file.write(entry + '\n')
    else:
        # If .gitignore does not exist, create it and add the entry
        with open(gitignore_path, 'w') as file:
            file.write(entry + '\n')


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