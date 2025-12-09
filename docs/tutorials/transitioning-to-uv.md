# Transitioning Any Repository to UV

This tutorial explains how to migrate any Python project from traditional virtual environment tools (venv, virtualenv, virtualenvwrapper) and pip to `uv`, a modern, fast Python package and project manager written in Rust.

## Why UV?

`uv` is designed to be a drop-in replacement for pip, pip-tools, and virtualenv, but significantly faster:

- **10-100x faster** than pip for package installation
- **Single tool** replaces pip, pip-tools, virtualenv, and more
- **Built-in dependency resolution** with proper lockfiles
- **Cross-platform** support (Windows, macOS, Linux)
- **Project-aware** with automatic virtual environment management

**Important Philosophy**: With `uv`, you should **never use `uv pip install`**. Instead, always use `uv add` to ensure your dependencies are properly tracked in `pyproject.toml` and locked in `uv.lock`.

## Prerequisites

### Installing UV

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

**Verify installation:**
```bash
uv --version
```

For more installation options, see: https://docs.astral.sh/uv/getting-started/installation/

## Step-by-Step Migration Guide

### Step 1: Deactivate and Remove Old Virtual Environment

If you have an active virtual environment, deactivate it first:

```bash
# Deactivate current virtual environment
deactivate

# Optional: Remove old virtual environments
# For virtualenvwrapper users:
rmvirtualenv your-env-name

# For standard venv users:
rm -rf venv/
rm -rf .venv/
```

### Step 2: Initialize UV Project

Navigate to your project root and initialize `uv`:

```bash
cd /path/to/your/project
uv init
```

This creates a `pyproject.toml` file if one doesn't exist. If your project already has a `pyproject.toml`, `uv` will use it.

### Step 3: Convert requirements.txt to pyproject.toml

If your project uses `requirements.txt` and `requirements-dev.txt`, you'll migrate these to `pyproject.toml`.

**For production dependencies:**

```bash
# Add each production dependency
# UV will automatically detect versions from requirements.txt
cat requirements.txt | grep -v "^#" | grep -v "^$" | xargs -I {} uv add {}
```

**For development dependencies:**

```bash
# Add dev dependencies with --dev flag
cat requirements-dev.txt | grep -v "^#" | grep -v "^$" | xargs -I {} uv add --dev {}
```

**Windows (cmd.exe) alternative:**

Since piping through grep/xargs doesn't work well on Windows, add dependencies manually:

```cmd
REM Read your requirements.txt and add each dependency
uv add package-name

REM For dev dependencies, read requirements-dev.txt and add each
uv add --dev package-name==version
```

**Manual approach (recommended for precision):**

Review your requirements files and add dependencies individually to ensure proper version constraints:

```bash
# Example: Add production dependencies
uv add requests numpy pandas

# Example: Add development dependencies with versions
uv add --dev pytest==9.0.1 black==25.11.0
```

### Step 4: Create Virtual Environment and Install Dependencies

UV automatically manages virtual environments:

```bash
# Create .venv/ and install all dependencies
uv sync
```

This command:
- Creates a `.venv/` directory in your project
- Installs all dependencies from `pyproject.toml`
- Generates a `uv.lock` lockfile for reproducible builds

### Step 5: Update .gitignore

Ensure your `.gitignore` includes:

```gitignore
# Virtual environments
.venv/
venv/
env/

# UV lockfile (commit this!)
# uv.lock should be committed for reproducible builds

# Old pip files (optional: keep for transition period)
# requirements.txt
# requirements-dev.txt
```

**Important**: Unlike many virtual environment files, you **should commit `uv.lock`** to version control. This ensures reproducible builds across environments.

### Step 6: Update Your Makefile (if applicable)

If your project uses a `Makefile`, update targets to use `uv run`:

**Key changes:**
- Replace `pip install -r requirements-dev.txt` with `uv sync`
- Prefix all Python commands with `uv run` (e.g., `uv run pytest`, `uv run black`)

Example:
```makefile
install-dev:
	uv sync

lint:
	uv run flake8 .
	uv run black --check .

test:
	uv run pytest
```

### Step 7: Update CI/CD Configuration

Update your GitHub Actions or other CI configuration to install and use UV:

**Key changes:**
```yaml
- name: Install UV
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv sync

- name: Run tests
  run: uv run pytest
```

### Step 8: Clean Up Old Files (Optional)

After confirming everything works:

```bash
# Backup old requirements files
git mv requirements.txt requirements.txt.bak
git mv requirements-dev.txt requirements-dev.txt.bak

# Or delete them entirely after testing
# rm requirements.txt requirements-dev.txt
```

## Daily UV Workflow

### Adding Dependencies

**Never use `uv pip install`!** Always use `uv add`:

```bash
# Add a production dependency
uv add requests

# Add with specific version
uv add "requests>=2.31.0"

# Add development dependency
uv add --dev pytest-mock

# Add multiple dependencies at once
uv add requests httpx pandas
```

### Running Commands

Use `uv run` to execute commands in the UV environment:

```bash
# Run Python scripts
uv run python main.py

# Run installed tools
uv run pytest
uv run black .
uv run flake8 src/

# Start Jupyter notebook
uv run jupyter notebook

# Build MkDocs site
uv run mkdocs serve
```

### Removing Dependencies

```bash
# Remove a package
uv remove requests

# Remove a dev dependency
uv remove --dev pytest-mock
```

### Updating Dependencies

```bash
# Update all dependencies
uv lock --upgrade

# Update specific package
uv lock --upgrade-package requests

# Sync to latest lockfile
uv sync
```

### Activating the Virtual Environment (Alternative)

While `uv run` is preferred, you can still activate the virtual environment manually:

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows (cmd.exe):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

## Understanding pyproject.toml Structure

After migration, your `pyproject.toml` contains:

- **`[project]`**: Project metadata and production dependencies
- **`[project.optional-dependencies]`**: Optional dependency groups
- **`[tool.uv]`**: UV-specific configuration and dev dependencies
- **`[build-system]`**: Build tool configuration

UV will manage this file automatically when you use `uv add` and `uv remove`.

## MkDocs Integration

Since you're using MkDocs:

```bash
# Add MkDocs (already in requirements.txt)
uv add mkdocs

# Add optional themes/plugins
uv add mkdocs-material

# Run MkDocs commands
uv run mkdocs serve
uv run mkdocs build
uv run mkdocs gh-deploy
```

## Troubleshooting

### "uv: command not found"

Ensure UV is in your PATH. Restart your terminal or add to shell config:

```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.bash_profile
export PATH="$HOME/.cargo/bin:$PATH"
```

On Windows, add UV's installation directory to System Environment Variables and restart your terminal.

### Dependencies not found after git pull

Always run `uv sync` after pulling changes:

```bash
git pull
uv sync
```

### Version conflicts

UV has better dependency resolution than pip. If you encounter conflicts:

```bash
# Clear lock and rebuild
rm uv.lock
uv lock
uv sync
```

### Windows-specific issues

On Windows, you may need to:
1. Run PowerShell as Administrator for initial setup
2. Set execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Manually add UV to PATH via System Environment Variables

## Migration Checklist

- [ ] Install `uv` on your system
- [ ] Deactivate and remove old virtual environments
- [ ] Run `uv init` in project root
- [ ] Migrate dependencies using `uv add` (read from requirements.txt)
- [ ] Migrate dev dependencies using `uv add --dev` (read from requirements-dev.txt)
- [ ] Run `uv sync` to create `.venv/` and install everything
- [ ] Update `.gitignore` to include `.venv/`
- [ ] Commit `uv.lock` to version control
- [ ] Update `Makefile` to use `uv run`
- [ ] Update CI/CD workflows to use `uv`
- [ ] Test all commands work with `uv run`
- [ ] Update project documentation (README, CONTRIBUTING)
- [ ] (Optional) Remove old `requirements.txt` files after confirming migration
- [ ] Verify all team members can run `uv sync` successfully

## Benefits After Migration

1. **Faster installations**: 10-100x faster than pip
2. **Better dependency management**: Proper lockfiles with `uv.lock`
3. **Simplified workflow**: One tool instead of multiple (pip, pip-tools, virtualenv)
4. **Reproducible builds**: Lockfiles ensure consistent environments across machines
5. **Modern tooling**: Built on Rust for speed and reliability
6. **Project-aware**: UV understands your project structure automatically
7. **No more `requirements.txt` confusion**: Everything centralized in `pyproject.toml`

## Additional Resources

- **UV Documentation**: https://docs.astral.sh/uv/
- **UV GitHub Repository**: https://github.com/astral-sh/uv
- **UV Getting Started Guide**: https://docs.astral.sh/uv/getting-started/
- **pyproject.toml Specification**: https://peps.python.org/pep-0621/
- **UV vs pip Compatibility**: https://docs.astral.sh/uv/pip/compatibility/

Welcome to modern Python development with UV!
