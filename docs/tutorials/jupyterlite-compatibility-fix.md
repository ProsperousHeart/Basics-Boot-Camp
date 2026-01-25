# Fixing JupyterLite Compatibility Issues

## The Problem

When using the `mkdocs-jupyterlite` plugin to embed interactive Jupyter notebooks in your MkDocs site, you may encounter two issues:

1. **Images don't display** - images referenced in notebooks may not display correctly (whether through relative path or via HTML)
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

After JupyterLite Plugin (WITHOUT our fix):
site/jupyterlite/files/
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references ../../IMGs/image1.png ✗ Broken (no IMGs folder!)

After JupyterLite Plugin (WITH our hook):
site/jupyterlite/files/
├── IMGs/              ← Our hook copies this!
│   ├── image1.png
│   └── image2.png
└── BC_Weeks/
    └── Week_1/
        └── notebook.ipynb  → references ../../IMGs/image1.png ✓ Works!
```

### Why Images Break

JupyterLite uses a **virtual filesystem** served via an API, not regular static files. When a notebook references `../../IMGs/image.png`:

1. JupyterLite tries to fetch via its contents API
2. The API returns 404 because IMGs wasn't included in the virtual filesystem
3. Image shows briefly (browser tries direct path) then breaks (API takes over)

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

Learn more about hooks [here](./git-hooks-pre-push-validation.md).

For this solution, we use an `on_post_build` hook to:

- modify the **built copies** of notebooks, leaving source files unchanged
- copy the IMGs folder after JupyterLite has finished copying notebooks

### What The Hook Does

1. **Replaces relative image paths** with GitHub raw URLs
2. **Changes kernel name** from `python3` to `python` for Pyodide

### Configuration

Add this to `mkdocs.yml`:

```yaml
hooks:
  - hooks/copy_images.py
```

### Implementation

Create `hooks/copy_images.py` in the project root:

```python title="hooks/copy_images.py"
--8<-- "hooks/copy_images.py"
```

The hook also includes built-in verification that prints the number of files copied. Look for this message in your build output:

```
✓ Copied X files from docs/IMGs to site/jupyterlite/files/IMGs
```

## How It Works

### Build Process Flow

This is an abbreviated flow for the purposes of this specific tutorial.

```
┌─────────────────────────────────────────────────────────────┐
│  MkDocs Build Process Timeline                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. MkDocs processes markdown files                         │
│     ↓                                                       │
│  2. JupyterLite plugin copies notebooks to:                 │
│     site/jupyterlite/files/BC_Weeks/Week_X/*.ipynb          │
│     ↓                                                       │
│  3. on_post_build hook runs                                 │
│     → Finds all .ipynb files in jupyterlite/files/          │
│     → Replaces ../../IMGs/ with GitHub raw URL              │
│     → Replaces "python3" kernel with "python"               │
│     ↓                                                       │
│  4. Build complete!                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

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

## Why This Approach?

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Embed images as base64** | Always works | Huge file sizes (686KB image = 915K chars) |
| **Copy IMGs folder to site** | Simple | JupyterLite API doesn't serve static files |
| **Modify source notebooks** | Permanent fix | Breaks local Jupyter usage |
| **GitHub raw URLs via hook** | Works everywhere, source unchanged | Requires internet |

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

### ❌ Option 2: Duplicate Images in Each Week Folder

**Approach**: Copy images to each `Week_X/IMGs/` folder

**Pros**:
- Notebooks can use `./IMGs/image.png`

**Cons**:
- Massive file duplication
- Harder to maintain/update images
- Increases repository size significantly

### ✅ Option 3: Use MkDocs Hook (Our Solution)

**Approach**: Copy IMGs folder during build process

**Pros**:
- No notebook changes required
- Maintains DRY principle (single image source)
- Works with existing relative paths
- Minimal overhead

**Cons**:
- Requires understanding hooks
- Adds build step complexity (minimal)

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

2. **Verify paths in deployed site**: Images should be at `/jupyterlite/files/IMGs/`

3. **Check if IMGs folder was copied**:
   ```bash
   ls site/jupyterlite/files/IMGs/
   ```

4. **Verify hook is registered**:
   Check `mkdocs.yml` has `hooks: - hooks/copy_images.py`

5. **Check build output**:
   Look for "✓ Updated X JupyterLite notebooks" message

6. **Inspect browser console**:
   Open DevTools → Console, look for 404 errors on images

7. **Verify relative paths in notebooks**:
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

1. **Check mkdocs.yml** - Ensure `hooks: - hooks/copy_images.py` is present

2. **Check file path** - Hook must be at `hooks/copy_images.py` relative to project root

3. **Check for Python errors** - Run `python hooks/copy_images.py` to syntax check

4. **Hook function name** - Must be exactly `on_post_build`

5. **File permissions**: Ensure hook file is readable

6. **Clear cache**: Try `mkdocs build --clean`

## Customization

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

### MkDocs Hooks

- [MkDocs Hooks Guide](https://www.mkdocs.org/dev-guide/plugins/#events)
- [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [MkDocs Build Process](https://www.mkdocs.org/dev-guide/themes/#template-variables)

### JupyterLite Resources

- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [mkdocs-jupyterlite Plugin](https://github.com/NickCrews/mkdocs-jupyterlite)
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
