from setuptools import setup, find_packages

setup(
    name="django_superapp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Django >= 5.0.0",
        "django-unfold >= 0.22.0",
        "django-svelte-jsoneditor >= 0.4.2",
        "django-import-export >= 4.0.3",
        "django-admin-confirm >= 1.0.0",
    ],
)
