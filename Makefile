all: help

.PHONY: help
# help
help:
	@echo "This Makefile provides useful commands for development"

# venv
venv:
	python3 -m virtualenv venv

.PHONY: install
# install
install:
	python setup.py install

.PHONY: test
# test
test:
	python setup.py test
