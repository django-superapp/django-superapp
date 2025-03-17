import os
import re
from pathlib import Path

import click
import yaml
from copier import run_copy, run_update, Worker

from .utils import sync_directories, clone_repo, open_repo_in_github, create_pr, remove_directory_if_exists
import tempfile

def validate_github_repo(ctx, param, value):
    # Regular expressions for GitHub repository URLs
    github_https_regex = r'^https:\/\/github\.com\/[a-zA-Z0-9\-_]+\/[a-zA-Z0-9\-_]+$'
    github_ssh_regex = r'^git@github\.com:[a-zA-Z0-9\-_]+\/[a-zA-Z0-9\-_]+\.git$'

    # Check if the value matches either regex
    if not re.match(github_https_regex, value) and not re.match(github_ssh_regex, value):
        raise click.BadParameter('The repository URL must be a valid GitHub HTTPS or SSH URL.')

    return value


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--template-repo',
    default='https://github.com/django-superapp/django-superapp-default-project',
    callback=validate_github_repo,
    help='SuperApp GitHub repository URL.'
)
@click.argument('target_directory')
def bootstrap_project(template_repo, target_directory):
    """Bootstrap a project into target directory."""

    run_copy(
        template_repo,
        str(target_directory),
        data={'project_name': os.path.basename(target_directory)},
    )


@cli.command()
@click.option(
    '--template-repo',
    callback=validate_github_repo,
    help='SuperApp GitHub repository URL.'
)
@click.argument('target_directory')
def bootstrap_app(template_repo, target_directory):
    """Create an app inside the project."""
    current_directory = os.getcwd()
    if not current_directory.endswith("superapp/apps"):
        raise click.ClickException(
            "You must run this command inside the 'superapp/apps' directory."
        )

    run_copy(
        template_repo,
        str(target_directory),
        data={'app_name': os.path.basename(target_directory)},
    )


@cli.command()
@click.argument('target_directory')
def pull_template(target_directory):
    """Update the local template with the remote changes."""

    run_update(
        str(target_directory),
        overwrite=True,
    )


@cli.command()
@click.argument('target_directory')
def push_template(target_directory):
    """Push the local changes to the remote template."""
    fork_directory = tempfile.mkdtemp()
    try:
        with Worker(dst_path=Path(target_directory)) as worker:
            repo_url = worker.subproject.last_answers.get('_src_path')

        try:
            with open(f"{target_directory}/copier.yml", 'r') as file:
                copier_configuration = yaml.safe_load(file)
        except OSError:
            copier_configuration = {}

        if not repo_url:
            raise click.ClickException(
                "The target directory does not have a remote repository configured."
            )

        click.echo(f"Forking the repository in {fork_directory} directory...")
        clone_repo(
            repo_url=repo_url,
            target_directory=fork_directory,
        )

        click.echo("Syncing the directories...")
        sync_directories(
            src=target_directory,
            dst=fork_directory,
            copier_configuration=copier_configuration,
        )

        open_repo_in_github(fork_directory)
        click.secho("Do not commit sensitive information to the remote repository!", fg='yellow', bold=True)
        if not click.confirm('Have you pushed your commits to the remote repository?'):
            raise click.Abort()

        create_pr(fork_directory)
    except Exception as e:
        raise e
    finally:
        click.echo("Cleaning up...")
        remove_directory_if_exists(fork_directory)


if __name__ == '__main__':
    cli()
