PYTHON ?= python
PIP := $(PYTHON) -m pip

.PHONY: help install-dev lint format test

help:
	@echo "Targets:"
	@echo "  install-dev  - install development dependencies"
	@echo "  lint         - run linters (flake8 + black --check)"
	@echo "  format       - run black to format code"
	@echo "  test         - run pytest"

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
	black src/ test/

test:
	@echo "Running pytest..."
	pytest -q
