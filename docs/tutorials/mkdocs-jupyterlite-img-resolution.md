# MkDocs, JupyterLite & Image Resolution: Complete Guide

!!! info "Comprehensive Solution Guide"
    This tutorial combines the complete journey of solving JupyterLite image display issues with MkDocs, from failed attempts to working solution.

## The Problem

When using the `mkdocs-jupyterlite` plugin to embed interactive Jupyter notebooks in your MkDocs site, you may encounter two issues:

1. **Images don't display** - images referenced in notebooks may not display correctly through relative path
2. **No kernel available** - notebooks specify `python3` but JupyterLite uses `python`

### File Structure Visualization

```
Before JupyterLite Plugin:
docs/
├── IMGs/
│   ├── image1.png
│   └── image2.png
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references ../../IMGs/image1.png ✓ Works

After JupyterLite Plugin (WITHOUT fix):
site/jupyterlite/files/
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references ../../IMGs/image1.png ✗ Broken (no IMGs folder!)

❌ ATTEMPTED SOLUTION (Copy IMGs Folder):
After JupyterLite Plugin (with folder copy attempt):
site/jupyterlite/files/
├── IMGs/              ← Hook copied this here
│   ├── image1.png
│   └── image2.png
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references ../../IMGs/image1.png ✗ Still broken!

After JupyterLite Plugin (WITH working fix):
site/jupyterlite/files/
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references GitHub raw URL ✓ Works!
```

### Why Images Break

JupyterLite uses a **virtual filesystem** served via an API, not regular static files. When a notebook references `../../IMGs/image.png`:

1. JupyterLite intercepts the request
2. JupyterLite tries to fetch via its contents API
3. The API returns 404 because IMGs wasn't included in the virtual filesystem (it doesn't serve static files this way)
4. Image shows briefly (browser tries direct path) then breaks (API takes over)

```
Browser Console Error:
GET /jupyterlite/api/contents/IMGs/all.json HTTP/1.1" code 404
```

### Why Kernels Don't Work

Your notebooks specify:
```json
"kernelspec": {
  "name": "python3"
}
```

But JupyterLite's Pyodide kernel is registered as `python`, not `python3`.

## The Solution: MkDocs Post-Build Hook

For this solution, we use an `on_post_build` hook to:

- modify the **built copies** of notebooks, leaving source files unchanged
- replace relative image paths with GitHub raw URLs for JupyterLite compatibility

### Understanding MkDocs Hooks

!!! info "Hooks vs Git Hooks"
    Don't confuse **MkDocs hooks** (Python functions that run during documentation builds) with **Git hooks** (scripts that run during Git operations). See [Git Hooks: Preventing Pipeline Failures](git-hooks-pre-push-validation.md) for Git hooks.

**MkDocs hooks** are Python functions that run at specific points during the documentation build process. They allow you to customize build behavior without creating a full plugin.

#### Common Hook Events

| Hook Event | When It Runs | Common Use Cases |
|------------|--------------|------------------|
| `on_startup` | Before anything else | Initialize resources, check dependencies |
| `on_config` | After config loads | Modify configuration dynamically |
| `on_pre_build` | Before build starts | Clean directories, prepare assets |
| `on_files` | When files are collected | Add/remove/modify file list |
| `on_post_build` | After build completes | **Copy assets, post-process files** ← We use this! |
| `on_page_markdown` | Before markdown rendering | Transform markdown content |
| `on_page_content` | After markdown to HTML | Modify HTML content |

### What The Solution Hook Does

1. **Replaces relative image paths** with GitHub raw URLs
2. **Changes kernel name** from `python3` to `python` for Pyodide

### Configuration

Add this to `mkdocs.yml`:

```yaml
hooks:
  - hooks/fix_notebook_img_issue.py
```

### Implementation

Create `hooks/fix_notebook_img_issue.py` in the project root:

```python title="hooks/fix_notebook_img_issue.py"
--8<-- "hooks/fix_notebook_img_issue.py"
```

The hook also includes built-in verification that prints the number of notebooks updated. Look for this message in your build output:

```
✓ Updated X JupyterLite notebooks (images + kernel)
```

## How It Works

### Build Process Flow

<div class="ascii-art">
```
┌─────────────────────────────────────────────────────────────┐
│  MkDocs Build Process Timeline                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. on_startup                                              │
│     ↓                                                       │
│  2. on_config                                               │
│     ↓                                                       │
│  3. on_pre_build                                            │
│     ↓                                                       │
│  4. on_files                                                │
│     ↓                                                       |
│  1. MkDocs processes markdown files → HTML                  │
│     ↓                                                       │
│  2. JupyterLite plugin copies notebooks to:                 │
│     site/jupyterlite/files/BC_Weeks/Week_X/*.ipynb          │
│     ↓                                                       │
│  3. on_post_build hook runs                                 │
│     → Finds all .ipynb files in jupyterlite/files/          │
│     → Replaces ../../IMGs/ with GitHub raw URL              │
│     → Replaces "python3" kernel with "python"               │
│     ↓                                                       │
│  4. Build complete! Site is ready to deploy.                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</div>

### Before and After

**Image paths:**

```
Before: ../../IMGs/learn-to-code-online.png
After:  https://raw.githubusercontent.com/ProsperousHeart/Basics-Boot-Camp/main/docs/IMGs/learn-to-code-online.png
```

**Kernel specification:**

```json
Before: "name": "python3"
After:  "name": "python"
```

## Why This Approach Works

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Embed images as base64** | Always works | Huge file sizes (686KB image = 915K chars) |
| **Copy IMGs folder to site** | Simple - no changes to source files | JupyterLite API doesn't serve static files<br>requires mkdocs hook<br>massive file duplication - increases repo size |
| **Modify source notebooks** (Use Absolute URLs in source) | Permanent fix<br>No extra hooks needed | Breaks local Jupyter usage<br>Requires internet<br>requires updating all notebooks<br>breaks if URL changes |
| **GitHub raw URLs via hook** | Works everywhere, source unchanged | Requires internet<br>breaks if URL changes |
| **Preload images into virtual FS** | Offline access, clean paths | Untested, increases bundle size |

### Why GitHub Raw URLs Work

- External URLs bypass JupyterLite's virtual filesystem
- Images are fetched directly from GitHub's CDN
- No API routing involved - just standard HTTP GET

## Alternative Solutions Considered

### ❌ Option 1: Use Absolute URLs

**Approach**: Change image paths to `https://yoursite.com/IMGs/image.png`

**Pros**:

- Works everywhere (local notebooks, JupyterLite, GitHub)

**Cons**:

- Couples notebooks to deployment URL
- Doesn't work offline
- Requires updating all notebooks
- Breaks if site URL changes

### ❌ Option 2: Use MkDocs Hook (Copy IMGs Folder - Attempted)

**Approach**: Copy IMGs folder during build process

**Pros**:

- No notebook changes required (notebooks can use `./IMGs/image.png`)
- Massive file duplication
- Maintains DRY principle (single image source)
- Works with existing relative paths (in theory)
- Increases repository size significantly

**Cons**:

- ❌ **Doesn't work with JupyterLite's virtual filesystem**
- Images still don't display despite being copied

**Why it fails**: Even after copying the IMGs folder to `site/jupyterlite/files/`, images still don't display because JupyterLite serves files through a **virtual filesystem API**, not direct HTTP requests.

When a notebook references `../../IMGs/image.png`:

1. JupyterLite intercepts the request
2. Tries to fetch via `/jupyterlite/api/contents/IMGs/image.png`
3. Returns 404 because the virtual filesystem API doesn't serve static files this way
4. Browser shows broken image despite folder being present

### ✅ Option 3: Use MkDocs Hook (URL Replacement - Working Solution)

**Approach**: Replace relative image paths with GitHub raw URLs during build

**Pros**:

- ✅ **Actually works with JupyterLite**
- No notebook source changes required
- Maintains DRY principle (single image source)
- Images served from reliable GitHub CDN
- Minimal overhead

**Cons**:

- Requires internet connection for images
- Couples to GitHub repository URL

### ❓ Option 4: Preload Images into Virtual File System (Untested)

**Approach**: Configure JupyterLite to pre-bundle images into its virtual filesystem

**Pros**:

- Images would be available offline
- No external dependencies
- Clean relative path access in notebooks
- Potentially simpler than build hooks

**Cons**:

- ❓ **Untested** - May not work with MkDocs integration
- Increases bundle size
- Requires JupyterLite configuration changes

**Implementation** (Untested):

```json
// In jupyterlite_config.json
{
  "LiteBuildConfig": {
    "files": ["docs/IMGs/"]
  }
}
```

**Usage in notebooks** (would be):

```python
from IPython.display import Image
Image("../files/IMGs/myplot.png")
```

!!! info "JupyterLite Files Configuration"
    The `files` option in `LiteBuildConfig` allows pre-bundling additional files into the JupyterLite virtual filesystem. See [JupyterLite Configuration Reference](https://jupyterlite.readthedocs.io/en/latest/reference/config.html#litebuildconfig) for details.

!!! warning "Untested Alternative"
    This approach was suggested by AI after our working solution was implemented. It may or may not work with the MkDocs JupyterLite plugin integration. Test thoroughly before adopting.

## Testing

### Local Testing

```bash
# Build the site
mkdocs build --clean

# Check the hook ran
# Look for: "✓ Updated X JupyterLite notebooks (images + kernel)"

# Serve locally
mkdocs serve
```

### Verify Changes Were Applied

Check a built notebook:

```bash
# Windows
type site\jupyterlite\files\BC_Weeks\Week_1\Python_Basics_04_-_Operators.ipynb | findstr "github"

# Linux/Mac
grep "github" site/jupyterlite/files/BC_Weeks/Week_1/Python_Basics_04_-_Operators.ipynb
```

Should show GitHub raw URLs instead of relative paths.

## Troubleshooting

### Images Still Not Showing

If your images still appear locally but not in deployment ...

1. **Check deployment process**: Ensure entire `site/` directory is deployed

2. **Verify notebook modifications**: Check that built notebooks contain GitHub raw URLs

3. **Verify hook ran**:
   Check build output for "✓ Updated X JupyterLite notebooks" message

4. **Verify hook is registered**:
   Check `mkdocs.yml` has `hooks: - hooks/fix_notebook_img_issue.py`

5. **Check GitHub URL accessibility**:
   Ensure the raw GitHub URLs work in browser

6. **Inspect browser console**:
   Open DevTools → Console, look for 404 errors on images

7. **Verify source notebooks**:
   Ensure notebooks use `../../IMGs/` not `../IMGs/` or other variants

8. **Clear browser cache** - JupyterLite caches aggressively

9. **Verify GitHub URL is correct** - Check the raw URL works in browser

10. **Check web server configuration**: Ensure proper MIME types for images

11. **CORS issues**: Check browser console for cross-origin errors

### Kernel Still Not Found

1. **Verify hook ran** - Check build output for update message

2. **Check notebook metadata** - Should show `"name": "python"` not `"python3"`

3. **Wait for Pyodide** - First load downloads ~15MB runtime; be patient

4. **Check browser console** - Look for Pyodide loading errors

### Hook Not Running

1. **Check mkdocs.yml** - Ensure `hooks: - hooks/fix_notebook_img_issue.py` is present

2. **Check file path** - Hook must be at `hooks/fix_notebook_img_issue.py` relative to project root

3. **Check for Python errors** - Run `python hooks/fix_notebook_img_issue.py` to syntax check

4. **Hook function name** - Must be exactly `on_post_build`

5. **File permissions**: Ensure hook file is readable

6. **Clear cache**: Try `mkdocs build --clean`

## Customization

!!! Warning
    All examples in this section are based on the structure of the repo. Actual customization may differ based on yours.

### Using a Different Image Location

Edit the constants at the top of the hook:

```python
# Change this to your repo's raw URL
GITHUB_RAW_BASE = (
    "https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/docs/IMGs/"
)

# Change this to match your notebook's relative paths
RELATIVE_IMG_PATH = "../../IMGs/"
```

### Using a Different Branch

If your default branch isn't `main`:

```python
GITHUB_RAW_BASE = (
    "https://raw.githubusercontent.com/ProsperousHeart/Basics-Boot-Camp/master/docs/IMGs/"
)
```

## Additional Resources

### MkDocs Documentation

- [MkDocs Hooks Guide](https://www.mkdocs.org/dev-guide/plugins/#events)
- [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [MkDocs Build Process](https://www.mkdocs.org/dev-guide/themes/#template-variables)

### JupyterLite Resources

- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [mkdocs-jupyterlite Plugin](https://github.com/NickCrews/mkdocs-jupyterlite)
- [JupyterLite Configuration](https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/config.html)
- [Pyodide Kernel](https://jupyterlite.readthedocs.io/en/latest/howto/python/pyodide.html)

### GitHub Raw URLs

- Format: `https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}`
- [GitHub Raw Content](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file#viewing-or-copying-the-raw-file-content)

### Python `shutil` Module

- [shutil Documentation](https://docs.python.org/3/library/shutil.html)
- [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree) - Copy entire directory trees
- [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree) - Remove directory trees

### Related Topics

- [Understanding Relative vs Absolute Paths](https://www.linux.com/training-tutorials/absolute-path-vs-relative-path-linuxunix/)
- [Python Pathlib Guide](https://realpython.com/python-pathlib/)
- [MkDocs Plugin Development](https://www.mkdocs.org/dev-guide/plugins/)
- [Git Hooks: Preventing Pipeline Failures](git-hooks-pre-push-validation.md)

## Summary

JupyterLite's virtual filesystem doesn't support relative paths to directories outside its content scope.

MkDocs hooks provide a powerful way to customize the build process without creating full plugins. By using the `on_post_build` hook, we ensure that images referenced in Jupyter notebooks remain accessible when notebooks are served through JupyterLite, maintaining the relative path structure that works in the original documentation.

By using an MkDocs post-build hook, we transform the built notebook copies to use:

1. **GitHub raw URLs** for images (bypasses virtual filesystem)
2. **Correct kernel name** (`python` for Pyodide compatibility)

This approach is:

- ✅ **Maintainable**: Single source of truth for images
- ✅ **Scalable**: Works for any number of notebooks/images
- ✅ **Clean**: No notebook modifications required
- ✅ **Efficient**: Minimal build overhead & no manual intervention (runs automatically on build)

### The Problem-Solving Journey

This solution evolved through multiple iterations:

1. **Initial Problem**: Images don't display in JupyterLite notebooks
2. **First Attempt**: Copy IMGs folder during build (seemed logical but failed)
3. **Root Cause Discovery**: JupyterLite's virtual filesystem API blocks direct file access
4. **Working Solution**: Replace relative paths with external GitHub raw URLs
5. **Additional Discovery**: Kernel name mismatch (`python3` vs `python`)

The journey demonstrates the importance of understanding platform-specific constraints and iterative problem-solving in complex integrations.</content>