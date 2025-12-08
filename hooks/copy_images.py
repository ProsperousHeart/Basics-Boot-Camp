# ABOUTME: MkDocs post build hook to copy IMGs folder to JupyterLite files dir
# ABOUTME: ensures image references (../../IMGs/) work in JupyterLite env

import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    """
    Copy IMGs folder to JupyterLite files directory after build completes.

    This hook runs after the MkDocs build finishes, copying the docs/IMGs
    directory to site/jupyterlite/files/IMGs so that relative image paths
    in Jupyter notebooks continue to work when served through JupyterLite.

    Args:
        config: MkDocs configuration dictionary containing:
            - docs_dir: Path to the docs directory
            - site_dir: Path to the built site directory
        **kwargs: Additional hook arguments (unused)
    """
    # Source: docs/IMGs
    source = Path(config["docs_dir"]) / "IMGs"

    # Destination: site/jupyterlite/files/IMGs
    dest = Path(config["site_dir"]) / "jupyterlite" / "files" / "IMGs"

    if source.exists():
        # Remove old IMGs directory if it exists to ensure clean copy
        if dest.exists():
            shutil.rmtree(dest)

        # Copy the entire IMGs directory tree
        shutil.copytree(source, dest)
        num_files = len(list(source.glob("**/*")))
        print(f"✓ Copied {num_files} files from {source} to {dest}")
    else:
        print(f"⚠ Warning: Source directory {source} does not exist")
