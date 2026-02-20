# Lesson Learned: JupyterLite Deployment Issues

This document explains multiple issues encountered when deploying JupyterLite to GitHub Pages, where Lab and Tree interfaces failed to load while the Notebooks interface worked correctly.

---

## The Problem

When hosting the site on GitHub Pages, only **Option 1 (Notebooks interface)** loaded correctly. **Option 2 (Lab interface)** and **Option 3 (Tree view)** showed blank pages or failed to initialize.

Locally, all three options appeared to work, making this a deployment-specific issue that was difficult to debug.

---

## Root Cause

Each JupyterLite interface (`/notebooks/`, `/lab/`, `/tree/`, etc.) has its own `jupyter-lite.json` configuration file. These files tell JupyterLite where to find its JavaScript bundles and other static assets.

The critical configuration property is `fullStaticUrl`, which points to the `../build` directory containing all the compiled JavaScript.

**The issue**: `lab/jupyter-lite.json` was missing the `fullStaticUrl` property.

### Configuration Comparison

| Interface | `fullStaticUrl` | Result |
|-----------|-----------------|--------|
| `/notebooks/` | `"../build"` ✅ | **Worked** |
| `/tree/` | `"../build"` ✅ | **Worked** |
| `/lab/` | **MISSING** ❌ | **Failed** |

Without `fullStaticUrl`, the Lab interface couldn't locate its JavaScript bundles, causing it to fail silently on GitHub Pages.

---

## The Fix

Added the missing `fullStaticUrl` property to `docs/jupyterlite/lab/jupyter-lite.json`:

**Before:**
```json
{
  "jupyter-lite-schema-version": 0,
  "jupyter-config-data": {
    "appUrl": "/lab",
    "settingsUrl": "../build/schemas",
    "showLoadingIndicator": true,
    "themesUrl": "./build/themes",
    "mode": "multiple-document"
  }
}
```

**After:**
```json
{
  "jupyter-lite-schema-version": 0,
  "jupyter-config-data": {
    "appUrl": "/lab",
    "fullStaticUrl": "../build",
    "settingsUrl": "../build/schemas",
    "showLoadingIndicator": true,
    "themesUrl": "./build/themes",
    "mode": "multiple-document"
  }
}
```

---

## Why It Worked Locally

Local development servers (like `mkdocs serve`) may handle relative path resolution differently than GitHub Pages. The browser's dev tools or network inspector might show 404 errors for JavaScript files when loading the Lab interface on production, but locally the paths may resolve correctly due to different base URL handling.

---

## Key Takeaways

1. **Check all interface configurations**: When JupyterLite builds, it creates multiple interfaces (`lab`, `notebooks`, `tree`, `repl`, `consoles`, `edit`). Each has its own `jupyter-lite.json` that may need consistent configuration.

2. **`fullStaticUrl` is critical**: This property tells JupyterLite where to find its compiled JavaScript bundles. Without it, the interface cannot load.

3. **Test on production-like environments**: Issues with relative paths and static asset resolution often only appear in production. Use `mkdocs build` and serve the `site/` directory with a simple HTTP server to catch these issues before deployment.

4. **Compare working vs non-working configs**: When one interface works and another doesn't, diff the configuration files to find missing properties.

---

## How to Debug Similar Issues

1. **Open browser DevTools** (F12) on the failing page
2. **Check the Network tab** for 404 errors on `.js` files
3. **Check the Console tab** for JavaScript errors
4. **Compare `jupyter-lite.json`** files between working and non-working interfaces
5. **Verify the `../build` directory** exists and contains the expected JavaScript bundles

---

## Issue 2: `.gitignore` Blocking Build Directory

### The Problem

Even after fixing the `fullStaticUrl` configuration, Lab and Tree interfaces still showed 404 errors for `bundle.js` files on GitHub Pages. The browser console showed:

```
GET .../jupyterlite/build/lab/bundle.js 404 (Not Found)
GET .../jupyterlite/build/tree/bundle.js 404 (Not Found)
```

### Root Cause

The project's `.gitignore` contained a generic `build/` rule (commonly used to ignore Python/Node build artifacts). This rule was inadvertently ignoring `docs/jupyterlite/build/` - the directory containing all JupyterLite JavaScript bundles.

```gitignore
# This rule in .gitignore:
build/

# Was ignoring:
docs/jupyterlite/build/   # All JS bundles needed for JupyterLite!
```

Running `git status --ignored` revealed the issue:

```
Ignored files:
    docs/jupyterlite/build/
```

### The Fix

Add an exception to `.gitignore` to un-ignore the JupyterLite build directory:

```gitignore
build/
!docs/jupyterlite/build/
```

Then add and commit the previously-ignored files:

```bash
git add docs/jupyterlite/build/
git commit -m "Add JupyterLite build files for deployment"
```

---

## Issue 3: Gitleaks False Positives

### The Problem

After adding the `docs/jupyterlite/build/` directory to git, the gitleaks security scan failed with 6 "generic-api-key" alerts:

```
Finding:     ...t.FourKeyMap=void 0;class i{construct...
Secret:      REDACTED
RuleID:      generic-api-key
File:        docs/jupyterlite/build/3462.a328105.js
```

### Root Cause

Gitleaks flagged `FourKeyMap` - a JavaScript class name in xterm.js (a terminal library used by JupyterLite). The word "Key" triggered the generic-api-key rule, but this refers to map/dictionary keys, not cryptographic or API keys.

**Why it's a false positive:**

- `FourKeyMap` is a data structure class with methods like `set(e,t,s,r,o)` and `get(e,t,i,s)`
- Low entropy (3.875) - real secrets have high randomness
- Doesn't match any known secret patterns (AWS `AKIA*`, GitHub `ghp_*`, etc.)
- It's third-party open-source code from xterm.js

### The Fix

Create a `.gitleaks.toml` configuration file to exclude the JupyterLite build directory:

```toml
# .gitleaks.toml
[extend]
useDefault = true

[[allowlists]]
description = "JupyterLite build directory - minified JS with false positive class names"
paths = [
    '''docs/jupyterlite/build/.*''',
]
```

**Note:** Gitleaks does NOT use `.gitleaksignore` files. It requires a `.gitleaks.toml` file with TOML syntax.

---

## Summary of All Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing `fullStaticUrl` | Lab/Tree show blank | Add `"fullStaticUrl": "../build"` to `jupyter-lite.json` |
| `.gitignore` blocking build | 404 errors for `bundle.js` | Add `!docs/jupyterlite/build/` exception |
| Gitleaks false positives | Security scan fails | Create `.gitleaks.toml` with path allowlist |

---

## Related Files

- `docs/jupyterlite/jupyter-lite.json` - Root configuration
- `docs/jupyterlite/lab/jupyter-lite.json` - Lab interface config (fixed)
- `docs/jupyterlite/notebooks/jupyter-lite.json` - Notebooks interface config (reference)
- `docs/jupyterlite/tree/jupyter-lite.json` - Tree interface config (reference)
- `.gitignore` - Added exception for JupyterLite build
- `.gitleaks.toml` - Gitleaks allowlist configuration
