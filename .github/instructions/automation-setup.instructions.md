# Automation Setup Instructions

**Last Updated**: 2025-11-09

This document provides guidance for automating documentation updates and workflow processes using GitHub Actions, pre-commit hooks, and manual scripts.

## 🎯 Overview

This template supports three automation approaches:
1. **GitHub Actions** - CI/CD automation on push/PR
2. **Pre-commit Hooks** - Local validation before commits
3. **Manual Scripts** - On-demand execution

Each approach has enable/disable options and examples below.

## 🤖 GitHub Actions Automation

### What Can Be Automated

- Documentation index updates (`docs/INDEX.md`)
- Cross-reference table updates (`docs/SPEC-CROSS-REFERENCE.md`)
- README synchronization
- Diagram generation
- Test execution
- Ruff linting and formatting
- Security scanning

**TODO**: Add complete automation list

### Example: Auto-Update Documentation

Create `.github/workflows/update-docs.yml`:

```yaml
name: Update Documentation

on:
  push:
    paths:
      - 'docs/requirements/**'
      - 'docs/specifications/**'
      - 'src/**'
  pull_request:
    paths:
      - 'docs/requirements/**'
      - 'docs/specifications/**'
      - 'src/**'

jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install UV
        run: pip install uv

      - name: Update Documentation Index
        run: python scripts/update-index.py

      - name: Update Cross-Reference Table
        run: python scripts/update-cross-reference.py

      - name: Commit Changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add docs/INDEX.md docs/SPEC-CROSS-REFERENCE.md
          git diff --staged --quiet || git commit -m "docs: auto-update documentation index and cross-references"

      - name: Push Changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

**TODO**: Add complete workflow examples

### Enabling/Disabling

**Enable**: Place workflow file in `.github/workflows/`
**Disable**: Remove or rename to `.github/workflows-disabled/`

**TODO**: Add workflow management script

## 🪝 Pre-commit Hooks Automation

### What Can Be Automated

- Ruff formatting
- Ruff linting
- Test execution
- Documentation validation
- Cross-reference table validation

**TODO**: Add complete hook list

### Example: Pre-commit Configuration

Create or update `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: local
    hooks:
      - id: validate-docs
        name: Validate Documentation
        entry: python scripts/validate-docs.py
        language: system
        files: 'docs/.*\.md$'
        pass_filenames: false

      - id: update-cross-reference
        name: Update Cross-Reference Table
        entry: python scripts/update-cross-reference.py
        language: system
        files: '(docs/requirements/.*|docs/specifications/.*|src/.*|test/.*)\.md$'
        pass_filenames: false

      - id: run-tests
        name: Run Tests
        entry: pytest
        language: system
        pass_filenames: false
        stages: [commit]
```

**TODO**: Add complete pre-commit configuration

### Installation

```bash
# Install pre-commit
pip install pre-commit

# or with uv
uv add --dev pre-commit

# Install hooks
pre-commit install
```

### Enabling/Disabling

**Enable specific hook**: Edit `.pre-commit-config.yaml` and set `stages: [commit]`
**Disable specific hook**: Comment out or remove from `.pre-commit-config.yaml`
**Disable all hooks temporarily**: `git commit --no-verify`
**Uninstall hooks**: `pre-commit uninstall`

**TODO**: Add hook management guide

## 📜 Manual Scripts Automation

### Available Scripts

Create `scripts/` directory with automation scripts:

```
scripts/
├── update-index.py              # Update docs/INDEX.md
├── update-cross-reference.py    # Update docs/SPEC-CROSS-REFERENCE.md
├── validate-docs.py             # Validate documentation structure
├── generate-threat-model.py     # Generate threat models
├── generate-architecture.py     # Generate architecture diagrams
└── README.md                    # Scripts usage guide
```

**TODO**: Implement actual scripts

### Example: Update Index Script

```python
#!/usr/bin/env python3
"""
ABOUTME: This script automatically updates the master documentation index.
ABOUTME: It scans docs/ folders and regenerates INDEX.md with current files.
"""

import os
from pathlib import Path
from datetime import datetime

def update_index():
    """Update docs/INDEX.md with current documentation structure."""
    docs_path = Path("docs")
    index_path = docs_path / "INDEX.md"

    # TODO: Implement index generation logic
    # - Scan requirements/
    # - Scan specifications/
    # - Scan diagrams/
    # - Update INDEX.md

    print(f"Updated {index_path}")

if __name__ == "__main__":
    update_index()
```

**TODO**: Implement complete scripts

### Usage

```bash
# Update documentation index
python scripts/update-index.py

# Update cross-reference table
python scripts/update-cross-reference.py

# Validate all documentation
python scripts/validate-docs.py

# Generate threat model
python scripts/generate-threat-model.py --requirement req-auth

# Generate architecture diagram
python scripts/generate-architecture.py --specification spec-auth
```

**TODO**: Add comprehensive usage examples

### Enabling/Disabling

**Enable**: Scripts are always available
**Disable**: N/A (manual execution only)

## 🔄 Automation Comparison

| Feature | GitHub Actions | Pre-commit Hooks | Manual Scripts |
|---------|----------------|------------------|----------------|
| **Trigger** | Push/PR | Git commit | Manual |
| **Speed** | Slower (CI) | Fast (local) | Fast (local) |
| **Consistency** | High | Medium | Low |
| **Flexibility** | High | Medium | High |
| **Team Sync** | Automatic | Requires setup | Manual |
| **Enable/Disable** | File presence | Config + install | Always available |

## ✅ Recommended Setup

### For Solo Developers
- ✅ Manual scripts (full control)
- ✅ Pre-commit hooks (optional, for consistency)
- 🟡 GitHub Actions (optional, for backups)

### For Small Teams
- ✅ Pre-commit hooks (shared standards)
- ✅ GitHub Actions (team sync)
- ✅ Manual scripts (flexibility)

### For Large Teams
- ✅ GitHub Actions (required, enforced)
- ✅ Pre-commit hooks (required, consistent)
- ✅ Manual scripts (troubleshooting)

**TODO**: Add team-size specific recommendations

## 🐛 Troubleshooting

### GitHub Actions not triggering

**TODO**: Add troubleshooting steps

### Pre-commit hooks failing

**TODO**: Add troubleshooting steps

### Scripts not finding files

**TODO**: Add troubleshooting steps

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [UV Environment Setup](uv-environment-setup.instructions.md)
- [Error Resolution KB](../../docs/rules/error-resolution-kb.md)

---

**TODO**: This is a placeholder. Expand with:
- Complete GitHub Actions workflows
- Full pre-commit configuration
- All automation scripts implemented
- Troubleshooting guide
- Performance optimization tips
