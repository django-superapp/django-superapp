import os
import click
import requests
from copier import run_copy, run_update
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


superapp_templates = get_superapp_templates()


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--project-template',
    type=click.Choice([
        project_name for project_name in superapp_templates.projects.keys()
    ], case_sensitive=False),
    default=[
        project_name for project_name in superapp_templates.projects.keys()
        if superapp_templates.projects[project_name].default
    ][0],
    show_default=True,
    show_choices=True,
    prompt=True,
)
@click.argument('target_directory')
def create_project(project_template, target_directory):
    """Bootstrap a project into target directory."""

    # Get the chosen project details
    project_template_obj = superapp_templates.projects[project_template]

    run_copy(
        project_template_obj.repo,
        str(target_directory),
        vcs_ref=project_template_obj.branch,
        data={
            'project_template': project_template,
            'project_template_obj': project_template_obj,
        },
        **(project_template_obj.kwargs or {}),
    )


@cli.command()
@click.argument('target_directory')
def update_project(target_directory):
    """Update a project with remote changes."""

    run_update(
        str(target_directory),
        overwrite=True,
    )


@cli.command()
@click.option(
    '--app-template',
    type=click.Choice([
        slug for slug in superapp_templates.apps.keys()
    ]),
    help='Name of the application template to use',
    show_choices=True,
    prompt=True,

)
def create_app(app_template):
    """Create an app inside the project."""
    target_path = os.path.join("superapp", "apps", app_template)

    if not os.path.exists("superapp/apps"):
        raise click.ClickException(
            "The superapp/apps directory does not exist. Make sure you are in the root of the project."
        )

    # Get the chosen project details
    app_template = superapp_templates.apps[app_template]

    run_copy(
        app_template.repo,
        str(target_path),
        vcs_ref=app_template.branch,
        **(app_template.kwargs or {}),
    )


@cli.command()
@click.argument('target_directory')
def update_app(target_directory):
    """Update a project with remote changes."""

    run_update(
        str(target_directory),
        overwrite=True,
    )

if __name__ == '__main__':
    cli()
