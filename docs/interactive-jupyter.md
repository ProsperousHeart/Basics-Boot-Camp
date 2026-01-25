<a href='http://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Interactive Jupyter Notebooks

Experience Python programming hands-on with our interactive notebook environment powered by JupyterLite!

## What is JupyterLite?

JupyterLite brings the full Jupyter experience to your browser with:

- ✅ **No installation required** - runs entirely in your browser
- ✅ **No server needed** - powered by [WebAssembly](https://webassembly.org/) ([Pyodide](https://pyodide.com/))
- ✅ **Full Python support** - execute real Python code
- ✅ **All course notebooks** - practice with the same materials
- ✅ **Persistent storage** - your work is saved in browser storage

## Launch Interactive Lab

!!! tip "Why Does This Open in a New Tab?"
    The creator of this bootcamp decided to force this interactive JupyterLite to open in a **new browser tab** rather than being embedded in this page for important technical reasons:

    - **Service Workers**: JupyterLite uses service workers for offline functionality, which require their own browsing context
    - **Browser Security**: Cross-origin restrictions (CORS/CSP) prevent proper iframe embedding
    - **URL Routing**: The full Jupyter interface needs control over URL navigation for file management
    - **Local Storage**: JupyterLite stores your work in browser storage, which works best in its own tab
    - **Better Experience**: Running in a dedicated tab provides more screen space and prevents interference with site navigation

    This ensures JupyterLite works reliably across all browsers and provides the best user experience!

<div style="text-align: center; margin: 2em 0;">
  <a href="../jupyterlite/lab/index.html" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 12px 24px; background-color: #3f51b5; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">
    🚀 Launch JupyterLite Lab (Opens in New Tab)
  </a>
</div>

## Available Notebooks

All bootcamp notebooks are available in the interactive environment:

### Week 1: Python Basics
- Introduction
- Syntax & Basic Statements
- Variables & Garbage Collection
- Operators, Decision Making, Sequences
- Numbers, Strings, Lists, Tuples, Dictionaries
- Type Conversions

### Week 2: Functions & Modules
- Iterators & Generators
- Functions
- Scope of Variables
- Modules

### Week 3: I/O & Exceptions
- Input & Output
- Exceptions & Assertions
- Additional Links

## How to Use

1. **Click the Launch button** above to open JupyterLite
2. **Navigate to the content folder** to find course notebooks
3. **Open any notebook** by double-clicking
4. **Run cells** by pressing `Shift + Enter`
5. **Experiment freely** - your changes won't affect the original files

## Tips for Using JupyterLite

### Running Code
- Press `Shift + Enter` to run the current cell and move to the next
- Press `Ctrl + Enter` to run the current cell without moving
- Use the "Run" menu for more options

### Keyboard Shortcuts
- `Esc` - Enter command mode
- `Enter` - Enter edit mode
- `A` - Insert cell above (command mode)
- `B` - Insert cell below (command mode)
- `DD` - Delete cell (command mode)
- `M` - Convert to markdown (command mode)
- `Y` - Convert to code (command mode)

### Saving Your Work
- JupyterLite saves notebooks in your browser's local storage
- Download notebooks to your computer using File → Download
- **Note:** Clearing browser data will delete your saved notebooks

### Limitations
- Some Python packages may not be available in the browser environment
- File I/O operations work with virtual filesystem
- Performance may be slower than native Python

## Prefer Local Development?

If you'd rather run notebooks on your local machine:

1. Install Jupyter:
   ```bash
   pip install jupyter
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/ProsperousHeart/Basics-Boot-Camp.git
   cd Basics-Boot-Camp
   ```

3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Troubleshooting

**Notebook won't load?**
- Check your internet connection
- Try refreshing the page
- Clear browser cache and try again

**Code not running?**
- Wait for the kernel to fully initialize (check the kernel indicator)
- Try restarting the kernel: Kernel → Restart

**Lost your work?**
- Check browser local storage hasn't been cleared
- Download notebooks frequently to back up your work

**Want to reset a notebook to its original state?**

JupyterLite saves all changes to your browser's local storage, which is great for preserving your work but means notebooks won't automatically reset when you reload the site. Here are several ways to reset:

1. **Reset Individual Notebook** (Recommended):
   - Open the notebook you want to reset
   - Go to `File → Revert Notebook to Checkpoint`
   - Or delete the notebook in JupyterLite and refresh to get a fresh copy

2. **Clear All JupyterLite Data** (Nuclear Option):
   - In JupyterLite, go to `Settings → Advanced Settings Editor`
   - Click `State Database` in the left panel
   - Click the "Clear State" button
   - Refresh the page

3. **Clear Browser Storage** (Most Thorough):
   - **Chrome/Edge**: Press `F12` → `Application` tab → `Storage` → `Clear site data`
   - **Firefox**: Press `F12` → `Storage` tab → Right-click → `Delete All`
   - Or use browser settings: `Settings → Privacy → Clear browsing data → Cookies and site data`
   - Then refresh the page

4. **Download Fresh Copy**:
   - If you want to keep your modified version AND have a clean copy
   - Download the original notebook from the [GitHub repository](https://github.com/ProsperousHeart/Basics-Boot-Camp/tree/main/docs/BC_Weeks)
   - Upload it to JupyterLite with a different name

**Note:** These reset methods only affect YOUR browser. Other users' notebooks remain unchanged.

## Support

Need help with the interactive environment?
- Check the [JupyterLite documentation](https://jupyterlite.readthedocs.io/)
- Ask questions in the community Discord
- Reach out on [LinkedIn](https://linkedin.com/in/kkeeton/)

---

**Ready to start coding?** <a href="../jupyterlite/lab/index.html" target="_blank" rel="noopener noreferrer">Launch JupyterLite Lab</a> and dive in!
