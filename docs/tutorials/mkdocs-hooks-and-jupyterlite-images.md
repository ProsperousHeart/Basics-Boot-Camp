# MkDocs Hooks and JupyterLite Image Handling

## The Problem

When using the `mkdocs-jupyterlite` plugin to embed interactive Jupyter notebooks in your MkDocs site, images referenced in notebooks may not display correctly. This happens because:

1. **Notebooks are in**: `docs/BC_Weeks/Week_X/notebook.ipynb`
2. **Images are in**: `docs/IMGs/`
3. **Notebooks use relative paths**: `../../IMGs/image.png` (which works in the original location)
4. **JupyterLite copies notebooks to**: `site/jupyterlite/files/BC_Weeks/Week_X/`
5. **But the IMGs folder is NOT copied**, breaking the relative paths

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

## The Solution: MkDocs Hooks

### What Are MkDocs Hooks?

**MkDocs hooks** are Python functions that run at specific points during the documentation build process. They allow you to customize build behavior without creating a full plugin.

### Common Hook Events

| Hook Event | When It Runs | Common Use Cases |
|------------|--------------|------------------|
| `on_startup` | Before anything else | Initialize resources, check dependencies |
| `on_config` | After config loads | Modify configuration dynamically |
| `on_pre_build` | Before build starts | Clean directories, prepare assets |
| `on_files` | When files are collected | Add/remove/modify file list |
| `on_post_build` | After build completes | **Copy assets, post-process files** ← We use this! |
| `on_page_markdown` | Before markdown rendering | Transform markdown content |
| `on_page_content` | After markdown to HTML | Modify HTML content |

### Our Hook Implementation

We use the `on_post_build` hook to copy the IMGs folder after JupyterLite has finished copying notebooks.

**Implementation**: See [`hooks/copy_images.py`](../../hooks/copy_images.py) in the project root.

**Configuration**: `mkdocs.yml`

```yaml
hooks:
  - hooks/copy_images.py
```

## How It Works

### Build Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│  MkDocs Build Process Timeline                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. on_startup                                             │
│     ↓                                                       │
│  2. on_config                                              │
│     ↓                                                       │
│  3. on_pre_build                                           │
│     ↓                                                       │
│  4. on_files                                               │
│     ↓                                                       │
│  5. Process markdown files → HTML                          │
│     ↓                                                       │
│  6. JupyterLite plugin copies notebooks to:                │
│     site/jupyterlite/files/BC_Weeks/Week_X/*.ipynb        │
│     ↓                                                       │
│  7. ✅ on_post_build (OUR HOOK RUNS HERE)                  │
│     → Copies docs/IMGs/ to site/jupyterlite/files/IMGs/   │
│     ↓                                                       │
│  8. Build complete! Site is ready to deploy.               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Why Relative Paths Work

When a notebook at `site/jupyterlite/files/BC_Weeks/Week_1/notebook.ipynb` references `../../IMGs/image.png`:

1. Start at: `site/jupyterlite/files/BC_Weeks/Week_1/`
2. Go up one level (`..`): `site/jupyterlite/files/BC_Weeks/`
3. Go up another level (`..`): `site/jupyterlite/files/`
4. Enter IMGs folder: `site/jupyterlite/files/IMGs/`
5. Access image: `site/jupyterlite/files/IMGs/image.png` ✓

## Testing the Fix

### Local Testing

```bash
# Build the site
mkdocs build

# Check if IMGs were copied
ls site/jupyterlite/files/IMGs/

# Serve locally and test notebooks
mkdocs serve
```

Then open a notebook in your browser and verify images display correctly.

### Automated Verification

The hook in [`hooks/copy_images.py`](../../hooks/copy_images.py) includes built-in verification that prints the number of files copied. Look for this message in your build output:

```
✓ Copied X files from docs/IMGs to site/jupyterlite/files/IMGs
```

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

## Additional Resources

### MkDocs Documentation

- [MkDocs Hooks Guide](https://www.mkdocs.org/dev-guide/plugins/#events)
- [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [MkDocs Build Process](https://www.mkdocs.org/dev-guide/themes/#template-variables)

### JupyterLite Resources

- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [mkdocs-jupyterlite Plugin](https://github.com/NickCrews/mkdocs-jupyterlite)
- [JupyterLite Configuration](https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/config.html)

### Python `shutil` Module

- [shutil Documentation](https://docs.python.org/3/library/shutil.html)
- [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree) - Copy entire directory trees
- [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree) - Remove directory trees

### Related Topics

- [Understanding Relative vs Absolute Paths](https://www.linux.com/training-tutorials/absolute-path-vs-relative-path-linuxunix/)
- [Python Pathlib Guide](https://realpython.com/python-pathlib/)
- [MkDocs Plugin Development](https://www.mkdocs.org/dev-guide/plugins/)

## Troubleshooting

### Images Still Not Showing

1. **Check if IMGs folder was copied**:
   ```bash
   ls site/jupyterlite/files/IMGs/
   ```

2. **Verify hook is registered**:
   Check `mkdocs.yml` has `hooks: - hooks/copy_images.py`

3. **Check build output**:
   Look for "✓ Copied X files from ..." message

4. **Inspect browser console**:
   Open DevTools → Console, look for 404 errors on images

5. **Verify relative paths in notebooks**:
   Ensure notebooks use `../../IMGs/` not `../IMGs/` or other variants

### Hook Not Running

1. **Python syntax errors**: Check [`hooks/copy_images.py`](../../hooks/copy_images.py) for errors
2. **File permissions**: Ensure hook file is readable
3. **Hook function name**: Must be exactly `on_post_build`
4. **Clear cache**: Try `mkdocs build --clean`

### Images Appear Locally But Not in Deployment

1. **Check deployment process**: Ensure entire `site/` directory is deployed
2. **Verify paths in deployed site**: Images should be at `/jupyterlite/files/IMGs/`
3. **Check web server configuration**: Ensure proper MIME types for images
4. **CORS issues**: Check browser console for cross-origin errors

## Summary

MkDocs hooks provide a powerful way to customize the build process without creating full plugins. By using the `on_post_build` hook, we ensure that images referenced in Jupyter notebooks remain accessible when notebooks are served through JupyterLite, maintaining the relative path structure that works in the original documentation.

This approach is:
- ✅ **Maintainable**: Single source of truth for images
- ✅ **Scalable**: Works for any number of notebooks/images
- ✅ **Clean**: No notebook modifications required
- ✅ **Efficient**: Minimal build overhead
