include version/Makefile.version

PYTHON = python3.6

all: help

.PHONY: help
# help
help:
	@echo "This Makefile provides useful commands for development"

# venv
venv:
	$(PYTHON) -m virtualenv venv

.PHONY: install
# install
install:
	python setup.py install

.PHONY: test
# test
test:
	python setup.py test
