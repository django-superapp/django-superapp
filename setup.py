import os
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

PACKAGE_NAME = os.getenv("PACKAGE_NAME", "django-superapp")

setup(
    name=PACKAGE_NAME,
    packages=find_packages(where="src"),
    description="Build your startup's product faster.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/django-superapp/django-superapp",
    author="Django SuperApp",
    author_email="django-superapp@bringes.io",
    license="MIT",
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'django_superapp=django_superapp.cli.main:cli',
        ],
    },
    install_requires=[
        "Django >= 5.0.0",
        "click >= 8.1.7",
        "copier >= 9.2.0",
        "sysrsync >= 1.1.1",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    project_urls={
        "Bug Reports": "https://github.com/django-superapp/django-superapp/issues",
        "Source": "https://github.com/django-superapp/django-superapp",
    },
)
