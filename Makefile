PYTHON ?= python
PIP := $(PYTHON) -m pip

.PHONY: help install-dev lint format test docs-build docs-serve docs-clean

help:
	@echo "Targets:"
	@echo "  install-dev  - install development dependencies"
	@echo "  lint         - run linters (flake8 + black --check)"
	@echo "  format       - run black to format code"
	@echo "  test         - run pytest"
	@echo "  docs-build   - build JupyterLite and MkDocs site"
	@echo "  docs-serve   - serve MkDocs site locally with live reload"
	@echo "  docs-clean   - clean built documentation files"

install-dev:
	$(PIP) install --upgrade pip
	@echo "Installing project requirements (if present)..."
	-$(PIP) install -r requirements-dev.txt
	-$(PIP) install -r requirements.txt
	@echo "Installing common dev tools..."
	$(PIP) install flake8 black pytest

lint:
	@echo "Running flake8..."
	flake8 .
	@echo "Checking formatting with black..."
# 	black --check src/ test/ || (echo "Black check failed — run 'make format' to fix." && exit 1)
	black --check HW/ || (echo "Black check failed — run 'make format' to fix." && exit 1)

format:
	@echo "Formatting with black..."
# 	black src/ test/
	black HW/

test:
	@echo "Running pytest..."
	pytest -q

docs-build:
#	@echo "Building JupyterLite interactive environment..."
#	mkdir docs\jupyterlite
# 	uv run jupyter lite build --contents Week_1 --contents Week_2 --contents Week_3 --output-dir docs/jupyterlite
	@echo "Building MkDocs site with JupyterLite plugin..."
	uv run mkdocs build
	@echo "Documentation built successfully! Open site/index.html to view."

docs-serve:
	@echo "Starting MkDocs development server..."
	@echo "Visit http://127.0.0.1:8000 to view the site"
	@echo "Press Ctrl+C to stop the server"
	uv run mkdocs serve

docs-clean:
	@echo "Cleaning documentation build files..."
	rm -rf site/
	rm -rf docs/jupyterlite/
	@echo "Documentation cleaned!"
