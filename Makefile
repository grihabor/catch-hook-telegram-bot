REPOSITORY_URL    = http://pypi.org/legacy
PYTHON            = python3.6
PYPI_DEPLOY_ATTRS = -p $(PYPI_PASSWORD) -u $(PYPI_USER)

all: help
include version/Makefile.version

.PHONY: help
help:
	@echo "This Makefile provides useful commands for development"

venv:
	$(PYTHON) -m virtualenv venv

.PHONY: install
install:
	python setup.py install

.PHONY: test
test:
	python setup.py test

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: wheel
wheel:
	python setup.py bdist_wheel

.PHONY: deploy
deploy:
	twine upload $(PYPI_DEPLOY_ATTRS) dist/*
