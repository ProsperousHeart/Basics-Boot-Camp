# MkDocs File Structure & Configuration

## How MkDocs Handles Files Outside docs/

### The Short Answer
**MkDocs automatically includes ANY files referenced in the `nav:` section of `mkdocs.yml`, regardless of where they are located in your project.**

No additional packages or configuration needed!

### How It Works

When you run `mkdocs build` or `mkdocs serve`:

1. MkDocs reads the `mkdocs.yml` configuration file
2. It scans the `nav:` section for all file references
3. It copies ALL referenced files to the build output, preserving their paths
4. Files can be anywhere in your project - they don't have to be in `docs/`

### Our Configuration

In our `mkdocs.yml`, we reference files from multiple locations:

```yaml
nav:
  - Home: index.md                          # In docs/
  - Getting Started:
    - getting-started/index.md              # In docs/getting-started/
    - Helpful Hints: Helpful_Hints.md       # In root directory!
  - Week 1 - Python Basics:
    - docs/BC_Weeks/Week_1/index.md                       # Inside docs/BC_Weeks/ folder
    - 01 - Introduction: docs/BC_Weeks/Week_1/Python_Basics_01_-_Introduction.ipynb
    # ... more notebooks from docs/BC_Weeks/Week_1/
  - Week 2 - Functions & Modules:
    - docs/BC_Weeks/Week_2/index.md                       # Inside docs/BC_Weeks/ folder
    # ... notebooks from docs/BC_Weeks/Week_2/
  - Week 3 - I/O & Exceptions:
    - docs/BC_Weeks/Week_3/index.md                       # Inside docs/BC_Weeks/ folder
    # ... notebooks from docs/BC_Weeks/Week_3/
  - Homework:
    - HW/READM.md                          # Outside docs/ folder!
  - Tutorials:
    - docs/tutorials/index.md               # In docs/tutorials/
```

### Complete File Organization

```
Basics-Boot-Camp/
├── mkdocs.yml                    # MkDocs configuration
├── Makefile                      # Automation commands
├── docs/                         # Documentation folder
│   ├── index.md                 # Main landing page
│   ├── getting-started/         # Getting started guide
│   │   └── index.md
│   ├── tutorials/               # Tutorial guides
│   │   ├── index.md
│   │   └── *.md files
│   ├── guidelines/              # MkDocs guides (this folder!)
│   │   ├── mkdocs-setup-guide.md
│   │   ├── mkdocs-file-structure.md
│   │   └── mkdocs-workflow.md
│   ├── home/                    # Home page sections
│   │   ├── course-structure.md
│   │   ├── enrollment.md
│   │   └── *.md files
│   ├── interactive-jupyter.md   # JupyterLite page
│   ├── IMGs/                    # Images used across the site
│   │   └── *.png files
│   ├── jupyterlite/             # Generated JupyterLite app
│   │   └── (generated files)
│   └── BC_Weeks/                # Course content
│       ├── Week_1/
│       │   ├── index.md
│       │   └── *.ipynb
│       ├── Week_2/
│       │   ├── index.md
│       │   └── *.ipynb
│       └── Week_3/
│           ├── index.md
│           └── *.ipynb
├── HW/                           # Homework (outside docs/ - still included!)
│   └── Requirements/
│       └── *.md files
├── overrides/                    # Theme customizations
│   └── main.html
└── site/                         # Generated site output
```

### What Gets Included

**Included in the built site:**
- ✅ Any file listed in `nav:` section
- ✅ Files in `docs/` folder (even if not in nav)
- ✅ Images, assets, JavaScript, CSS referenced by included files
- ✅ Jupyter notebooks (converted to HTML by mkdocs-jupyter plugin)

**NOT included in the built site:**
- ❌ Files not in `docs/` and not referenced in `nav:`
- ❌ Hidden files and folders (starting with `.`)
- ❌ Files in `.gitignore`
- ❌ Build artifacts, virtual environments, etc.

### Navigation Structure

The navigation in `mkdocs.yml` determines how your file structure is presented to users:

1. **Home** (`docs/index.md`) - Landing page with bootcamp overview
   - Course Structure, Time Expectations, Training Philosophy, etc.
2. **About** (`docs/getting-started/`) - Getting started guide and lessons learned
3. **Interactive Notebooks** - Main course content
   - Interactive Jupyter page (`docs/interactive-jupyter.md`)
   - Week 1: 12 Python Basics lessons (`docs/BC_Weeks/Week_1/`)
   - Week 2: 4 Functions & Modules lessons (`docs/BC_Weeks/Week_2/`)
   - Week 3: 3 I/O & Exceptions lessons (`docs/BC_Weeks/Week_3/`)
4. **Tutorials** (`docs/tutorials/`) - Additional guides (UV, MkDocs features, helpful hints)

### Jupyter Notebook Support

This project uses a **dual-format approach** for notebooks:

1. **`.ipynb` files** - Used by JupyterLite for the interactive lab
2. **`.md` files** - Converted markdown versions rendered by MkDocs

**JupyterLite Plugin Configuration:**
```yaml
plugins:
  - jupyterlite:
      enabled: true
      notebook_patterns:
        - "BC_Weeks/**/*.ipynb"
```

**What this means:**
- `.ipynb` notebooks are available in the JupyterLite interactive lab
- `.md` markdown files are displayed in the main documentation site
- Both versions are maintained in parallel
- JupyterLite creates a browser-based Python environment with all notebooks

### Static Assets (Images, Files)

Images and other assets referenced in your markdown/notebooks are automatically included:

```markdown
<!-- Relative paths work from the file's location -->
![Alt text](../IMGs/screenshot.png)

<!-- Absolute URLs always work -->
![Alt text](https://github.com/user/repo/raw/main/image.png)
```

MkDocs will:
1. Find the referenced file
2. Copy it to the build output
3. Update the reference path

### Best Practices

#### 1. Organize by Purpose
```
docs/          # Documentation AND course content
  ├── BC_Weeks/Week_*/  # Course content (notebooks)
  ├── tutorials/        # Tutorials and guides
  └── IMGs/            # Images
HW/            # Assignments (outside docs/)
```

#### 2. Use Descriptive Paths
```yaml
# Good - clear structure
- Week 1: docs/BC_Weeks/Week_1/index.md

# Also good - explicit about content
- Tutorials: docs/tutorials/index.md
```

#### 3. Keep Assets Organized
```
docs/
  └── IMGs/    # Images used across the site
docs/BC_Weeks/Week_1/        # Week 1 specific content
  ├── images/  # Week 1 specific images
  └── *.ipynb
```

#### 4. Use Index Files
Each section should have an `index.md`:
```
docs/BC_Weeks/Week_1/
  └── index.md     # Overview of Week 1
docs/BC_Weeks/Week_2/
  └── index.md     # Overview of Week 2
docs/
  └── tutorials/
      └── index.md  # Overview of tutorials
```

### Common Questions

**Q: Do I need to move all my content into docs/?**
A: No! Just reference files in `nav:` and MkDocs handles the rest.

**Q: Will this work with Jupyter notebooks outside docs/?**
A: Yes! The `mkdocs-jupyter` plugin works with notebooks anywhere in your project.

**Q: What if I have files I don't want in the site?**
A: Simply don't list them in `nav:`. Files outside `docs/` are only included if explicitly referenced.

**Q: Can I use relative links between files?**
A: Yes, but be careful. MkDocs expects links relative to the site root after build. Use the `nav:` structure for navigation instead.

**Q: What about the .ipynb_checkpoints folders?**
A: MkDocs automatically ignores hidden folders (starting with `.`). No action needed!

### Verifying Your Setup

To verify files are being included:

```bash
# Serve the site locally
mkdocs serve

# Visit http://127.0.0.1:8000
# Navigate to different sections
# Check that notebooks render properly
```

Or build and inspect:

```bash
# Build the site
mkdocs build

# Check the site/ folder
ls -R site/

# You should see your Week_1, Week_2, Week_3 folders
# and all referenced files
```

### No Additional Packages Needed!

The packages we installed are sufficient:

- ✅ `mkdocs` - Core functionality
- ✅ `mkdocs-material` - Theme
- ✅ `mkdocs-jupyter` - Notebook support
- ✅ `mkdocs-section-index` - Section navigation
- ✅ `mkdocs-glightbox` - Image lightbox
- ✅ `pymdown-extensions` - Enhanced markdown

**These handle everything:**
- Files outside `docs/`
- Jupyter notebooks
- Images and assets
- Navigation structure

## Site Features & Generated Structure

The following features are enabled and affect the site structure:

### 🔍 Search
Full-text search across all content (automatically generated in `site/search/`)

### 📱 Responsive Design
Works on desktop, tablet, and mobile (Material theme CSS)

### 🌙 Dark Mode
Toggle between light and dark themes (Material theme feature)

### 💻 Code Copying
One-click code copying from examples (pymdown-extensions feature)

### 🎮 Interactive Lab
Run Python code in the browser via JupyterLite (in `docs/jupyterlite/`)

### 📊 Notebook Rendering
Beautiful HTML rendering of Jupyter notebooks (mkdocs-jupyter plugin)

## Deployment Structure

### GitHub Pages (Manual)
```bash
uv run mkdocs gh-deploy
```
Creates a `gh-pages` branch with the built site from `site/`

### GitHub Actions (Automated)
Create `.github/workflows/docs.yml` to auto-deploy on every push to main.

The built site structure:
```
site/
├── index.html              # Main page
├── BC_Weeks/
│   ├── Week_1/
│   │   ├── index.html
│   │   └── (notebook pages as HTML)
│   ├── Week_2/
│   └── Week_3/
├── assets/                 # CSS, JS, images
├── search/                 # Search index
└── (all other nav pages)
```

## Known Issues & Notes

### File Path Warnings

You may see warnings about files not found during build. This can happen when:
- Navigation paths reference files that don't exist yet
- File paths need adjustment for the docs directory structure

**The site still builds and works correctly!** The warnings can be ignored or fixed by adjusting file paths in `mkdocs.yml`.

### JupyterLite Directory

- The `docs/jupyterlite/` folder is generated and contains many files
- Add it to `.gitignore` if you don't want to commit generated files
- It needs to be present for the Interactive Lab page to work
- Regenerate it when notebooks change

### Summary

**Key Takeaway:** MkDocs is flexible about file locations. Reference any file in `nav:` and it will be included in your site, regardless of where it lives in your project structure. No special configuration required!

This makes it perfect for projects like ours where:
- Course content (BC_Weeks/Week_1, Week_2, Week_3) is organized separately
- Documentation about the site lives in `docs/`
- Everything comes together in one beautiful, searchable site

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [mkdocs-jupyter Plugin](https://github.com/danielfrg/mkdocs-jupyter)
- [Workflow Guide](mkdocs-workflow.md)
- [Setup Guide](mkdocs-setup-guide.md)
