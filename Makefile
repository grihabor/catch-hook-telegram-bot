PYTHON = python3.6

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
