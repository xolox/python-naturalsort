# Makefile for the 'naturalsort' module.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: November 2, 2015
# URL: https://github.com/xolox/python-naturalsort

# The following defaults are based on my preferences, but possible for others
# to override thanks to the `?=' operator.
WORKON_HOME ?= $(HOME)/.virtualenvs
VIRTUAL_ENV ?= $(WORKON_HOME)/naturalsort
ACTIVATE = . "$(VIRTUAL_ENV)/bin/activate"

# Sometimes I like to use Bash syntax extensions :-).
SHELL = bash

default:
	@echo "Makefile for the 'naturalsort' package"
	@echo
	@echo 'Commands:'
	@echo
	@echo '    make install   install the package in a virtual environment'
	@echo '    make reset     recreate the virtual environment'
	@echo '    make clean     cleanup all temporary files'
	@echo '    make test      run the unit test suite'
	@echo '    make coverage  run the tests, report coverage'
	@echo '    make check     check the coding style'
	@echo '    make publish   publish changes to GitHub/PyPI'
	@echo
	@echo 'Variables:'
	@echo
	@echo "    WORKON_HOME = $(WORKON_HOME)"
	@echo "    VIRTUAL_ENV = $(VIRTUAL_ENV)"

install:
	test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv "$(VIRTUAL_ENV)"
	test -x "$(VIRTUAL_ENV)/bin/pip" || ($(ACTIVATE) && easy_install pip)
	test -x "$(VIRTUAL_ENV)/bin/pip-accel" || ($(ACTIVATE) && pip install --quiet pip-accel)
	$(ACTIVATE) && pip uninstall --yes naturalsort &>/dev/null || true
	$(ACTIVATE) && pip install --quiet --editable .

reset:
	rm -Rf "$(VIRTUAL_ENV)"
	make --no-print-directory install

clean:
	rm -Rf build dist docs/build htmlcov

test: install
	test -x "$(VIRTUAL_ENV)/bin/tox" || ($(ACTIVATE) && pip-accel install --quiet tox)
	$(ACTIVATE) && tox

coverage: install
	$(ACTIVATE) && pip-accel install --quiet coverage
	$(ACTIVATE) && coverage run setup.py test
	$(ACTIVATE) && coverage report
	$(ACTIVATE) && coverage html

check: install
	test -x "$(VIRTUAL_ENV)/bin/flake8" || ($(ACTIVATE) && pip-accel install --quiet flake8-pep257)
	$(ACTIVATE) && flake8

publish:
	git push origin && git push --tags origin
	make clean && python setup.py sdist upload

.PHONY: default install reset clean test coverage check publish
