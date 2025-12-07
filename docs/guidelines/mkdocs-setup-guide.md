# MkDocs Setup Guide for Basics-Boot-Camp

## Overview

This guide will help you set up MkDocs to:
- Display markdown documentation
- Render Jupyter notebooks
- **Run Jupyter notebooks interactively in the browser** using JupyterLite
- Provide a clean, navigable interface for your Python bootcamp materials

## Required MkDocs Plugins

### Core Plugins

1. **mkdocs-material** - Modern, responsive theme
2. **mkdocs-jupyter** - Converts Jupyter notebooks to HTML for display
3. **mkdocs-literate-nav** - Better navigation management
4. **mkdocs-section-index** - Makes section pages clickable

### Interactive Notebook Execution

For running notebooks in the browser, you have two main options:

#### Option A: JupyterLite (Recommended for Interactive Execution)
- **jupyterlite-sphinx** or integrate JupyterLite separately
- Runs Python entirely in the browser using WebAssembly (Pyodide)
- No backend server required
- Best for educational content

#### Option B: Thebe (Alternative)
- **mkdocs-thebe** - Connect to a Jupyter kernel
- Requires a JupyterHub or Binder backend
- More complex setup but supports more libraries

**For your use case, I recommend JupyterLite** as it's self-contained and perfect for bootcamp materials.

## Installation Steps

### 1. Install Dependencies

Add these to your `requirements-dev.txt` or install directly:

```bash
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-jupyter
pip install mkdocs-literate-nav
pip install mkdocs-section-index
pip install mkdocs-glightbox  # For image lightbox
pip install pymdown-extensions  # Enhanced markdown
```

For JupyterLite integration:
```bash
pip install jupyterlite-core
pip install jupyterlite-pyodide-kernel
```

### 2. Create MkDocs Configuration

Create a `mkdocs.yml` file in your repository root:

```yaml
site_name: Python Basics Boot Camp
site_description: Python Basics Boot Camp Training Materials
site_author: Prosperous Heart
site_url: https://yoursite.com  # Update with your URL

repo_name: ProsperousHeart/Basics-Boot-Camp
repo_url: https://github.com/ProsperousHeart/Basics-Boot-Camp
edit_uri: edit/main/

theme:
  name: material
  palette:
    # Light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.tracking
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.code.annotate

plugins:
  - search
  - mkdocs-jupyter:
      include_source: True
      execute: False  # Don't execute notebooks during build
      allow_errors: False
      ignore_h1_titles: True
  - literate-nav:
      nav_file: SUMMARY.md
  - section-index
  - glightbox  # Image lightbox

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
  - admonition
  - tables
  - toc:
      permalink: true

extra:
  social:
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/kkeeton/
    - icon: fontawesome/brands/github
      link: https://github.com/ProsperousHeart

nav:
  - Home: index.md
  - Getting Started:
    - Introduction: getting-started/index.md
    - Helpful Hints: Helpful_Hint.md
  - Week 1 - Python Basics:
    - Week_1/index.md
    - 01 - Introduction: Week_1/Python_Basics_01_-_Introduction.ipynb
    - 02 - Syntax & Statements: Week_1/Python_Basics_02_-_Syntax_And_Basic_Statements.ipynb
    - 03 - Variables & Garbage Collection: Week_1/Python_Basics_03_-_Variables_&_Garbage_Collection.ipynb
    - 04 - Operators: Week_1/Python_Basics_04_-_Operators.ipynb
    - 05 - Decision Making: Week_1/Python_Basics_05_-_Decision_Making.ipynb
    - 06 - Sequences: Week_1/Python_Basics_06_-_Sequences.ipynb
    - 07 - Numbers: Week_1/Python_Basics_07_-_Variable_Type_NUMBERS.ipynb
    - 08 - Strings: Week_1/Python_Basics_08_-_Variable_Type_STRING.ipynb
    - 09 - Lists: Week_1/Python_Basics_09_-_Variable_Type_LIST.ipynb
    - 10 - Tuples: Week_1/Python_Basics_10_-_Variable_Type_TUPLE.ipynb
    - 11 - Dictionaries: Week_1/Python_Basics_11_-_Variable_Type_DICTIONARY.ipynb
    - 12 - Type Conversions: Week_1/Python_Basics_12_-_Type_Conversions.ipynb
  - Week 2 - Functions & Modules:
    - Week_2/index.md
    - 13 - Iterators & Generators: Week_2/Python_Basics_13_-_Iterators_And_Generators.ipynb
    - 14 - Functions: Week_2/Python_Basics_14_-_Functions.ipynb
    - 15 - Scope of Variables: Week_2/Python_Basics_15_-_Scope_Of_Variables.ipynb
    - 16 - Modules: Week_2/Python_Basics_16_-_Modules.ipynb
  - Week 3 - I/O & Exceptions:
    - Week_3/index.md
    - 17 - Input & Output: Week_3/Python_Basics_17_-_Input_&_Output.ipynb
    - 18 - Exceptions & Assertions: Week_3/Python_Basics_18_-_Exceptions_&_Assertions.ipynb
    - 19 - Additional Links: Week_3/Python_Basics_19_-_Additional_Links.ipynb
  - Homework:
    - HW/README.md
  - Tutorials:
    - docs/tutorials/index.md
    - Clean Code Before PR: docs/tutorials/clean-code-before-pr.md
    - Makefile Windows Setup: docs/tutorials/makefile-windows-setup.md
    - Recreating Virtual Environments: docs/tutorials/recreating-virtual-environments-virtualwrapper.md
    - Transitioning to UV: docs/tutorials/transitioning-to-uv.md
  - Interactive Notebooks: jupyterlite/index.html
```

### 3. Create Index Pages

You'll need to create several index.md files:

**docs/index.md** (Main landing page - move/copy from README.md)
**getting-started/index.md** (Getting started guide)
**Week_1/index.md** (Week 1 overview)
**Week_2/index.md** (Week 2 overview)
**Week_3/index.md** (Week 3 overview)
**docs/tutorials/index.md** (Tutorials overview)

### 4. Setup JupyterLite for Interactive Notebooks

Create a separate JupyterLite build that MkDocs can link to:

```bash
# Create jupyterlite directory
mkdir jupyterlite
cd jupyterlite

# Copy your notebooks
mkdir content
cp -r ../Week_1/*.ipynb content/
cp -r ../Week_2/*.ipynb content/
cp -r ../Week_3/*.ipynb content/

# Build JupyterLite
jupyter lite build --contents content --output-dir ../docs/jupyterlite
```

Add to your MkDocs site by creating **docs/interactive.md**:

```markdown
# Interactive Jupyter Notebooks

Click the link below to launch an interactive Jupyter environment in your browser:

[Launch JupyterLite](jupyterlite/index.html){.md-button .md-button--primary}

## Available Notebooks

All course notebooks are available in the interactive environment:
- Week 1: Python Basics
- Week 2: Functions & Modules
- Week 3: I/O & Exceptions

No installation required - runs entirely in your browser!
```

### 5. Build and Serve

```bash
# Development server with live reload
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages (optional)
mkdocs gh-deploy
```

## Alternative: Embed Interactive Cells

If you want interactive cells embedded directly in the documentation pages, use **Thebe**:

```bash
pip install sphinx-thebe
```

Add custom JavaScript to enable Thebe in MkDocs Material theme by creating `docs/javascripts/thebe-config.js`.

However, this requires a backend (Binder/JupyterHub) which is more complex.

## Recommended File Structure

```
Basics-Boot-Camp/
├── mkdocs.yml
├── docs/
│   ├── index.md (from README.md)
│   ├── getting-started/
│   │   └── index.md
│   ├── tutorials/
│   │   ├── index.md
│   │   └── *.md files
│   ├── interactive.md
│   └── jupyterlite/ (built by JupyterLite)
├── Week_1/
│   ├── index.md
│   └── *.ipynb
├── Week_2/
│   ├── index.md
│   └── *.ipynb
├── Week_3/
│   ├── index.md
│   └── *.ipynb
├── HW/
│   └── README.md
└── Helpful_Hints.md
```

## Summary: Suggested Navigation Structure

### Main Navigation Tabs

1. **Home** - Landing page with bootcamp overview
2. **Getting Started** - Installation, setup, expectations
3. **Week 1** - Python Basics (12 lessons)
4. **Week 2** - Functions & Modules (4 lessons)
5. **Week 3** - I/O & Exceptions (3 lessons)
6. **Homework** - Implementation assignments
7. **Tutorials** - Additional guides and tips
8. **Interactive Lab** - JupyterLite for hands-on practice

### Key Features

- **Progressive Learning**: Organized by week for structured learning
- **Dual Mode**: Read notebooks as documentation OR run them interactively
- **Search**: Full-text search across all content
- **Mobile-Friendly**: Responsive design works on all devices
- **Dark Mode**: Eye-friendly theme switching
- **Code Copy**: One-click code copying from examples

### User Flow

1. Start at Home → understand bootcamp structure
2. Getting Started → set up local environment
3. Week 1/2/3 → read lessons sequentially
4. Interactive Lab → practice with live notebooks
5. Homework → apply what you learned
6. Tutorials → solve common problems

## Next Steps

Recommended implementation order:

1. Create the `mkdocs.yml` configuration file with your specific settings
2. Generate the index.md files for each section
3. Set up the JupyterLite integration
4. Create a GitHub Actions workflow for automatic deployment
5. Test locally with `mkdocs serve`
6. Deploy to GitHub Pages with `mkdocs gh-deploy`

## Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [mkdocs-jupyter Plugin](https://github.com/danielfrg/mkdocs-jupyter)
- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
