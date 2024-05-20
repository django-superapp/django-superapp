import os
import click
import requests
from copier import run_copy
from pydantic import ValidationError

from django_superapp.types import SuperAppTemplate


def get_superapp_templates() -> SuperAppTemplate:
    url = "https://raw.githubusercontent.com/django-superapp/django-superapp/main/superapp_templates.json"
    response = requests.get(url)
    response.raise_for_status()
    try:
        return SuperAppTemplate.parse_obj(response.json())
    except ValidationError as e:
        print("Error parsing JSON:", e)
        raise


@click.group()
def cli():
    pass


@cli.command()
@click.argument('target_directory')
def create_project(target_directory):
    """Bootstrap a project into target directory."""
    superapp_templates = get_superapp_templates()

    click.echo("Available projects:")
    for slug, project in superapp_templates.projects.items():
        click.echo(f" - {slug}: {project.description}")

    project_choice = click.prompt(
        'Please choose a project',
        type=click.Choice([
            project_name for project_name in superapp_templates.projects.keys()
        ], case_sensitive=False),
        default=[
            project_name for project_name in superapp_templates.projects.keys()
            if superapp_templates.projects[project_name].default
        ][0],
        show_default=True,
        show_choices=True,
    )

    # Get the chosen project details
    project_template = superapp_templates.projects[project_choice]

    run_copy(
        project_template.repo,
        str(target_directory),
        vcs_ref=project_template.branch,
        **(project_template.kwargs or {}),
    )


@cli.command()
@click.option('--app-name', default=None, help='Name of the application to create')
def add_app(app_name):
    """Bootstrap a project into target directory."""
    superapp_templates = get_superapp_templates()

    if app_name:
        app_choice = app_name
    else:
        click.echo("Available apps:")
        for slug, app in superapp_templates.apps.items():
            click.echo(f" - {slug}: {app.description}")

        app_choice = click.prompt(
            'Please type the app name',
            type=click.Choice([
                slug for slug in superapp_templates.apps.keys()
            ], case_sensitive=False),
            show_choices=True,
        )

    target_path = os.path.join("superapp", "apps", app_choice)

    if not os.path.exists("superapp/apps"):
        os.makedirs("superapp/apps")

    # Get the chosen project details
    app_template = superapp_templates.apps[app_choice]

    run_copy(
        app_template.repo,
        str(target_path),
        vcs_ref=app_template.branch,
        **(app_template.kwargs or {}),
    )


if __name__ == '__main__':
    cli()
