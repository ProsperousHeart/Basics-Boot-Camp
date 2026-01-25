# ABOUTME: MkDocs post build hook to fix notebooks for JupyterLite compatibility
# ABOUTME: replaces image paths with GitHub URLs and fixes kernel name for Pyodide

from pathlib import Path

# GitHub raw URL base for images
GITHUB_RAW_BASE = (
    "https://raw.githubusercontent.com/ProsperousHeart/Basics-Boot-Camp/main/docs/IMGs/"
)

# Relative path pattern used in source notebooks
RELATIVE_IMG_PATH = "../../IMGs/"


def on_post_build(config, **kwargs):
    """
    Update notebooks in built JupyterLite for compatibility.

    Performs two transformations on built notebook copies:
    1. Replaces relative image paths with GitHub raw URLs
    2. Changes kernel name from 'python3' to 'python' for Pyodide compatibility

    Source notebooks remain unchanged - only the built copies are modified.

    Args:
        config: MkDocs configuration dictionary containing:
            - site_dir: Path to the built site directory
        **kwargs: Additional hook arguments (unused)
    """
    site_dir = Path(config["site_dir"])
    jupyterlite_files = site_dir / "jupyterlite" / "files"

    if not jupyterlite_files.exists():
        print("⚠ JupyterLite files directory not found, skipping notebook updates")
        return

    notebooks_updated = 0

    for notebook_path in jupyterlite_files.rglob("*.ipynb"):
        content = notebook_path.read_text(encoding="utf-8")
        modified = False

        # Fix image paths
        if RELATIVE_IMG_PATH in content:
            content = content.replace(RELATIVE_IMG_PATH, GITHUB_RAW_BASE)
            modified = True

        # Fix kernel name for Pyodide (python3 -> python)
        if '"name": "python3"' in content:
            content = content.replace('"name": "python3"', '"name": "python"')
            modified = True

        if modified:
            notebook_path.write_text(content, encoding="utf-8")
            notebooks_updated += 1

    if notebooks_updated > 0:
        print(f"✓ Updated {notebooks_updated} JupyterLite notebooks (images + kernel)")
    else:
        print("ℹ No notebooks needed updates")
