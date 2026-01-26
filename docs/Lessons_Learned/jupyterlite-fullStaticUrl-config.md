# Lesson Learned: JupyterLite `fullStaticUrl` Configuration

This document explains an issue where JupyterLite's Lab interface failed to load on GitHub Pages while the Notebooks interface worked correctly.

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

## Related Files

- `docs/jupyterlite/jupyter-lite.json` - Root configuration
- `docs/jupyterlite/lab/jupyter-lite.json` - Lab interface config (fixed)
- `docs/jupyterlite/notebooks/jupyter-lite.json` - Notebooks interface config (reference)
- `docs/jupyterlite/tree/jupyter-lite.json` - Tree interface config (reference)
