Set up or verify the UV virtual environment

This command ensures the development environment is properly configured.

**Usage:**
- /setup-env

**Process:**

Follow .github/instructions/uv-environment-setup.instructions.md

### 1. Check for Existing Environment

```bash
# Check if .venv exists
ls .venv
```

### 2. Create Environment (if needed)

```bash
# Create virtual environment
uv venv
```

### 3. Activate Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
# Install production dependencies
uv add -r requirements.txt

# Install development dependencies
uv add --dev -r requirements-dev.txt
```

### 5. Verify Installation

```bash
# Verify Python version
python --version

# Verify key packages
python -c "import pytest; import ruff; print('Environment OK')"
```

### 6. Install Pre-commit Hooks (if available)

```bash
# If pre-commit is set up
pre-commit install
```

**Important Notes:**

- Use `uv add <package>` to add new production packages (NOT `uv pip install`)
- Use `uv add --dev <package>` to add new development packages
- The uv tool is faster than pip and handles dependencies better
- Virtual environment must be activated before running commands

**Expected Output:**
- Virtual environment created/verified
- All dependencies installed
- Pre-commit hooks installed
- Environment ready for development

**Next Step:** Create requirements or implement specifications