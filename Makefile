SHELL := /bin/bash
#include .env.local
#export $(shell sed 's/=.*//' .env.local)

# Update PATH variable
PATH := $(PATH):/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin

venv: venv/touchfile

install-virtualenv:
	python -m pip install --break-system-packages --user virtualenv;

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv;
	touch venv/touchfile;

install-requirements: venv/touchfile
	. venv/bin/activate && python -m pip install -r requirements.txt

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

release: dist ## package and upload a release
	. venv/bin/activate && twine upload dist/*

dist: venv/touchfile clean ## builds source and wheel package
	. venv/bin/activate && python setup.py sdist
	. venv/bin/activate && python setup.py bdist_wheel
	ls -l dist

install: venv/touchfile clean ## install the package to the active Python's site-packages
	. venv/bin/activate && python setup.py install

