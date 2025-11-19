# UV Environment Setup Instructions

**Last Updated**: 2025-11-09

This instruction file provides guidance for managing Python virtual environments using `uv`. This process is referenced throughout multiple workflows.

## 🎯 Overview

UV is a fast Python package installer and resolver. This guide covers:
- Checking for existing virtual environments
- Creating new environments
- Installing packages properly with `uv add`

## ✅ Prerequisites

- UV installed: `pip install uv` or follow [UV installation guide](https://github.com/astral-sh/uv)
- Python 3.12+ available

## 📋 Step-by-Step Process

### 1. Check for Existing Virtual Environment

```bash
# Check if .venv directory exists
ls .venv

# Or check if virtual environment is activated
echo $VIRTUAL_ENV  # Linux/Mac
echo %VIRTUAL_ENV%  # Windows
```

**TODO**: Add platform-specific checks and verification steps

### 2. Create Virtual Environment (if not found)

```bash
# Create virtual environment with uv
uv venv

# Create with specific Python version
uv venv --python 3.12
```

**TODO**: Add troubleshooting for common creation errors

### 3. Activate Virtual Environment

```bash
# Linux/Mac
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat
```

**TODO**: Add activation verification steps

### 4. Install/Add Packages

**IMPORTANT**: Use `uv add` instead of `uv pip install`

```bash
# Add a package (preferred method)
uv add <package-name>

# Add multiple packages
uv add <package1> <package2> <package3>

# Add dev dependencies
uv add --dev <package-name>

# DON'T use pip install directly
# ❌ uv pip install <package>  # Wrong!
# ✅ uv add <package>           # Correct!
```

**Why `uv add` instead of `uv pip install`?**
- Automatically updates `pyproject.toml`
- Resolves dependencies correctly
- Maintains lock file integrity

**TODO**: Add examples for different package types and edge cases

## 🔄 Common Workflows

### Starting a New Project

```bash
# 1. Create environment
uv venv

# 2. Activate it
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\Activate.ps1  # Windows

# 3. Add initial packages
uv add pytest black ruff
```

**TODO**: Add template project initialization script

### Joining an Existing Project

```bash
# 1. Check for existing environment
ls .venv

# 2. If exists, activate it
source .venv/bin/activate

# 3. Sync dependencies from lock file
uv sync
```

**TODO**: Add sync verification and troubleshooting

### Adding New Dependencies

```bash
# 1. Ensure environment is activated
echo $VIRTUAL_ENV

# 2. Add package
uv add <package-name>

# 3. Verify installation
uv pip list | grep <package-name>
```

**TODO**: Add dependency conflict resolution

## 🐛 Troubleshooting

### Environment Not Found

**TODO**: Add steps to diagnose and fix missing environment

### Activation Issues

**TODO**: Add platform-specific activation troubleshooting

### Package Installation Failures

**TODO**: Add common package installation errors and solutions

### Lock File Conflicts

**TODO**: Add lock file resolution strategies

## 🤖 AI Assistant Integration

### For Claude Code

This instruction file should be referenced when:
- Starting code generation workflows
- Setting up new features
- Installing dependencies

**TODO**: Add specific Claude Code integration examples

### For GitHub Copilot

**TODO**: Add Copilot integration examples

## 📚 Related Documentation

- [UV Official Documentation](https://github.com/astral-sh/uv)
- [Master Workflow](master-workflow.md)
- [TDD Workflow](tdd-workflow.instructions.md)

## 📝 Quick Reference

```bash
# Environment Management
uv venv                    # Create environment
source .venv/bin/activate  # Activate (Linux/Mac)
deactivate                 # Deactivate

# Package Management
uv add <package>           # Add package
uv add --dev <package>     # Add dev package
uv sync                    # Sync from lock file
uv pip list                # List installed packages
uv pip freeze              # Export requirements
```

---

**TODO**: This is a placeholder. Expand with:
- Complete troubleshooting guide
- Platform-specific instructions
- Advanced UV features
- Integration with CI/CD
- Common error patterns and solutions
