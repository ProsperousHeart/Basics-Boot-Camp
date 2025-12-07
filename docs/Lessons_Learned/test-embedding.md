# Test: Embedding JupyterLite Notebooks

This page tests different approaches to embedding interactive Jupyter notebooks in MkDocs.

## ✅ Option 1: Notebooks Interface (Recommended)

**Simpler, cleaner interface** - Best for embedded notebooks

<div style="width: 100%; height: 600px; border: 2px solid blue;">
  <iframe
    src="../../jupyterlite/notebooks/index.html?path=BC_Weeks/Week_1/Python_Basics_01_-_Introduction.ipynb"
    width="100%"
    height="100%"
    frameborder="0">
  </iframe>
</div>

**Why this works:**
- Path includes folder structure: `BC_Weeks/Week_1/filename.ipynb`
- Notebooks interface is simpler than full Lab
- Less cluttered when embedded

---

## ✅ Option 2: Lab Interface (Full Features)

**Full JupyterLab experience** - More features, more cluttered when embedded

<div style="width: 100%; height: 600px; border: 2px solid green;">
  <iframe
    src="../../jupyterlite/lab/index.html?path=BC_Weeks/Week_1/Python_Basics_01_-_Introduction.ipynb"
    width="100%"
    height="100%"
    frameborder="0">
  </iframe>
</div>

**Why this works:**
- Same path as Option 1
- Includes file browser, terminal, and other Lab features
- Better for advanced users

---

## 📁 Option 3: Tree/File Browser

**For browsing files only** - Not for opening notebooks directly

<div style="width: 100%; height: 600px; border: 2px solid orange;">
  <iframe
    src="../../jupyterlite/tree/index.html"
    width="100%"
    height="100%"
    frameborder="0">
  </iframe>
</div>

**Note:** The Tree view is for *browsing* the file structure. To open a notebook from here, you would need to navigate to it in the tree, but it's better to use Options 1 or 2 directly.

---

## 🔗 Direct Links (No Embedding)

Alternative: Link directly to JupyterLite instead of embedding:

- [Notebooks View](../../jupyterlite/notebooks/index.html?path=BC_Weeks/Week_1/Python_Basics_01_-_Introduction.ipynb){:target="_blank"} - Opens in new tab
- [JupyterLab View](../../jupyterlite/lab/index.html?path=BC_Weeks/Week_1/Python_Basics_01_-_Introduction.ipynb){:target="_blank"} - Opens in new tab
- [Tree View - Browse all files](../../jupyterlite/tree/index.html){:target="_blank"} - Opens in new tab
- [JupyterLab - No file specified](../../jupyterlite/lab/index.html){:target="_blank"} - Opens in new tab

**Pros:** Clean interface, full-screen, no nested navigation
**Cons:** User leaves the MkDocs site (can use `{:target="_blank"}` to open in new tab)

---

## 🏆 Recommendation

**For this bootcamp, use Option 1 (Notebooks Interface)**:
- Cleaner embedded view
- Less cluttered than Lab
- MkDocs navigation stays visible
- Fully interactive

**Template for creating wrapper pages:**
```markdown
<iframe
  src="../../../jupyterlite/notebooks/index.html?path=BC_Weeks/Week_X/NOTEBOOK_NAME.ipynb"
  width="100%"
  height="800px"
  frameborder="0">
</iframe>
```

---

## 📝 Key Learnings

1. **Path must include folder structure**: `BC_Weeks/Week_1/filename.ipynb`
2. **Relative paths depend on file location**:
   - From `docs/Lessons_Learned/test-embedding.md` → `../../jupyterlite/`
   - From `docs/BC_Weeks/Week_1/lesson.md` → `../../../jupyterlite/`
3. **Tree view is for browsing, not opening** notebooks directly
4. **Notebooks interface is simpler** than Lab for embedded views
