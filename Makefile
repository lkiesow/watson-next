# Watson

PYTHON ?= python
PIP ?= pip

VENV = $(PYTHON) -m venv
VENV_ARGS = 
VENV_DIR = $(CURDIR)/.venv
VENV_WATSON_DIR = $(CURDIR)/data

all: install

$(VENV_DIR): requirements-dev.txt
	$(VENV) $(VENV_ARGS) "$(VENV_DIR)"
	echo "export WATSON_DIR=\"$(VENV_WATSON_DIR)\"" >> "$(VENV_DIR)"/bin/activate
	echo "set -x WATSON_DIR \"$(VENV_WATSON_DIR)\"" >> "$(VENV_DIR)"/bin/activate.fish
	"$(VENV_DIR)"/bin/pip install -U setuptools wheel pip
	"$(VENV_DIR)"/bin/pip install -Ur $<

.PHONY: env
env: $(VENV_DIR)

.PHONY: install
install:
	$(PYTHON) -m pip install .

.PHONY: install-dev
install-dev:
	$(PIP) install -r requirements-dev.txt
	$(PYTHON) -m pip install --editable .

.PHONY: check
check: clean
	pytest

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr

.PHONY: distclean
distclean: clean
	rm -fr *.egg *.egg-info/ .eggs/

.PHONY:
mostlyclean: clean distclean
	rm -rf "$(VENV_DIR)"

.PHONY: docs
docs: install-dev
	$(PYTHON) scripts/gen-cli-docs.py
	mkdocs build

.PHONY: completion-scripts
completion-scripts:
	scripts/create-completion-script.sh bash
	scripts/create-completion-script.sh zsh
