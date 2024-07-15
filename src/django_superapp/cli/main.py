import os
import re

import click
from copier import run_copy, run_update


def validate_github_repo(ctx, param, value):
    # Regular expression for GitHub repository URLs
    github_repo_regex = r'^https:\/\/github\.com\/[a-zA-Z0-9\-_]+\/[a-zA-Z0-9\-_]+$'

    # Check if the value matches the regex
    if not re.match(github_repo_regex, value):
        raise click.BadParameter('The repository URL must be a valid GitHub repository URL.')

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

    if not target_directory:
        target_directory = template_repo.split("/")[-1]

    run_copy(
        template_repo,
        str(target_directory),
        data={'project_name': os.path.basename(target_directory)},
    )


@cli.command()
@click.option(
    '--template-repo',
    default='https://github.com/django-superapp/django-superapp-default-project',
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

    if not target_directory:
        target_directory = template_repo.split("/")[-1]

    run_copy(
        template_repo,
        str(target_directory),
        data={'app_name': os.path.basename(target_directory)},
    )


@cli.command()
@click.argument('target_directory')
def update(target_directory):
    """Update the superapp project/app in the target directory with the latest remote changes."""

    run_update(
        str(target_directory),
        overwrite=True,
    )


if __name__ == '__main__':
    cli()
