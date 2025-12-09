# Understanding MkDocs Features in This Project

This guide explains the MkDocs configuration currently used in this Python Basics Boot Camp documentation site. For setup instructions, see the [MkDocs Setup Guide](../guidelines/mkdocs-setup-guide.md).

## The Difference Between These Guides

| Guide | Purpose | When to Use |
|-------|---------|-------------|
| [**MkDocs Setup Guide**](../guidelines/mkdocs-setup-guide.md) | Step-by-step installation and initial configuration | Setting up MkDocs from scratch |
| **This Guide** | Explains features already configured in this project | Understanding what features do and learning more |

**Think of it this way:**
- 📦 **Setup Guide** = "How to build the site"
- 📚 **This Guide** = "How the site works"

## Quick Reference

### What is MkDocs?

[MkDocs](https://www.mkdocs.org/) is a static site generator that creates beautiful documentation websites from Markdown files.

### What is Material for MkDocs?

[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) is a modern, responsive theme that makes your documentation look professional and provides advanced features.

## Announcement Banner

This project uses the Material for MkDocs announcement banner feature to display important messages across the top of every page.

### What It Does

The announcement banner displays site-wide notifications, updates, or calls-to-action in a prominent colored bar above the navigation. Users can dismiss it by clicking the X button, and their preference is saved in browser localStorage.

**Key features**:
- **Dismissible**: Users can close it with an X button (top right)
- **Persistent**: Once dismissed, stays hidden until user clears browser data
- **Site-wide**: Appears on every page of the documentation
- **HTML support**: Can include links, formatting, emojis, and styling
- **Mobile responsive**: Automatically adjusts for smaller screens

### How It's Configured

The announcement banner requires two configuration elements:

#### 1. Enable Custom Overrides (mkdocs.yml)

```yaml
theme:
  name: material
  custom_dir: overrides  # Enables custom template directory
```

This tells MkDocs to look in the `overrides/` directory for custom template files.

#### 2. Create Announcement Template (overrides/main.html)

```html
{% extends "base.html" %}

{% block announce %}
  <p>
    📢 <strong>New Interactive Jupyter Notebooks!</strong>
    Try out Python code directly in your browser - no installation required.
    <a href="{{ page.canonical_url }}interactive-jupyter/">Start Learning →</a>
  </p>
{% endblock %}
```

**Template breakdown**:
- `{% extends "base.html" %}` - Inherits from Material's base template
- `{% block announce %}` - Defines the announcement content block
- `<p>` - Paragraph containing your message (can include HTML)
- `{{ page.canonical_url }}` - Jinja2 variable for building relative URLs

### How to Customize

**Edit the message**: Modify the content inside `{% block announce %}` in `overrides/main.html`

**Example templates**:

**For deadlines:**
```html
{% block announce %}
  <p>
    ⏰ <strong>Assignment Due:</strong> Week 2 homework due December 15 at 11:59pm EST.
    <a href="{{ page.canonical_url }}homework/">Submit Now →</a>
  </p>
{% endblock %}
```

**For live events:**
```html
{% block announce %}
  <p>
    🎓 <strong>Live Q&A Session:</strong> Join us this Friday at 2pm ET.
    <a href="{{ page.canonical_url }}events/">Register Here →</a>
  </p>
{% endblock %}
```

**For surveys:**
```html
{% block announce %}
  <p>
    📝 Help us improve! Take our 2-minute course survey.
    <a href="https://forms.example.com/survey" target="_blank">Give Feedback →</a>
  </p>
{% endblock %}
```

**Multiple messages with rotation:**
```html
{% block announce %}
  <p>
    🆕 <strong>New:</strong> Week 3 content now available! |
    ⏰ <strong>Reminder:</strong> Week 2 homework due Friday |
    🎉 <strong>Thanks</strong> to all our students for the great participation!
  </p>
{% endblock %}
```

### How to Disable

**Option 1 - Hide banner temporarily:**
```html
{% block announce %}
  <!-- Banner disabled - uncomment to re-enable
  <p>Your message here</p>
  -->
{% endblock %}
```

**Option 2 - Remove banner completely:**
Delete or comment out the entire `{% block announce %}` section in `overrides/main.html`.

**Option 3 - Disable custom overrides:**
Remove `custom_dir: overrides` from `mkdocs.yml` (also disables other customizations).

### Styling and Customization

The banner's appearance is controlled by Material for MkDocs theme. The default styling includes:
- Indigo background color (matches your `primary` theme color)
- White text
- Full-width banner
- Automatic dismiss button on the right
- Smooth slide-down animation on page load

**To customize colors**, you would need to add custom CSS (see Customization Tips section below).

### Best Practices

**Keep it concise**: Banner messages should be short (1-2 sentences max)

**Use clear calls-to-action**: Include a link with action words like "Start", "Register", "Submit"

**Update regularly**: Keep content fresh and remove outdated announcements

**Test dismissibility**: Verify users can close the banner easily

**Mobile testing**: Check how the banner looks on smaller screens

### Use Cases for This Project

- Announcing new course weeks or modules
- Homework deadlines and submission reminders
- Live session or office hours schedules
- Course surveys and feedback requests
- Holiday/break schedules
- New feature announcements (like JupyterLite)
- Important updates or corrections to course material

### File Locations

| Component | File Path | Purpose |
|-----------|-----------|---------|
| Configuration | `mkdocs.yml` (line 15) | Enables `custom_dir: overrides` |
| Template | `overrides/main.html` | Defines announcement content |
| Documentation | `docs/tutorials/understanding-mkdocs-features.md` | This guide |

### Troubleshooting

**Banner not appearing?**
1. Check `custom_dir: overrides` is in `mkdocs.yml` under `theme:`
2. Verify `overrides/main.html` exists
3. Ensure content exists in `{% block announce %}`
4. Rebuild: `make docs-clean && make docs-build`
5. Clear browser cache and localStorage

**Banner appears but looks broken?**
- Check HTML syntax in `overrides/main.html`
- Verify all opening/closing tags match
- Test with simple text first, then add complexity

**Links not working?**
- Use `{{ page.canonical_url }}` for relative links
- Use full URLs for external links
- Add `target="_blank"` for external links

**Learn more**: [Material Announcement Bar](https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-header/#announcement-bar)

---

## Current Navigation Features

### Enabled in This Project

| Feature | What It Does | Visual Effect |
|---------|--------------|---------------|
| **`navigation.tabs`** | Creates tabs across the top for main sections | You see "Home", "Getting Started", "Tutorials" as tabs |
| **`navigation.sections`** | Groups related pages into collapsible sections | Sections like "Home" can expand/collapse |
| **`navigation.expand`** | Auto-expands all sections | Sidebar shows all pages without clicking |
| **`navigation.indexes`** | Makes section titles clickable | Click "Home" to go to home index page |
| **`navigation.top`** | Adds back-to-top button | Bottom-right button appears when scrolling |
| **`navigation.tracking`** | Updates URL with current heading | URL shows `#current-section` as you scroll |
| **`navigation.instant`** | Instant page loading (SPA) | Pages load without full refresh |
| **`navigation.path`** | Shows breadcrumb trail | Top of page shows "Home > Course Overview" |

**Learn more**: [Material Navigation Docs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/)

### Search Features

| Feature | What It Does |
|---------|--------------|
| **`search.suggest`** | Shows suggestions as you type in search |
| **`search.highlight`** | Highlights your search terms on pages |

**Learn more**: [Search Setup](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/)

### Content Features

| Feature | What It Does |
|---------|--------------|
| **`content.code.copy`** | Adds copy button to code blocks |
| **`content.code.annotate`** | Enables clickable annotations in code |

**Learn more**: [Code Blocks Reference](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)

### Table of Contents

| Feature | What It Does |
|---------|--------------|
| **`toc.follow`** | Auto-scrolls TOC sidebar to current section |

**Learn more**: [TOC Configuration](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#table-of-contents)

## Plugins Explained

### Search Plugin
```yaml
- search
```
**What it does**: Enables the search bar and full-text search across all pages.

**Learn more**: [MkDocs Search](https://www.mkdocs.org/user-guide/configuration/#search)

---

### Monorepo Plugin
```yaml
- monorepo
```
**What it does**: Allows managing multiple documentation projects in one repository.

**Why we use it**: Useful if you want to organize different parts of the bootcamp as separate "sub-projects."

**Learn more**: [mkdocs-monorepo-plugin](https://github.com/backstage/mkdocs-monorepo-plugin)

---

### JupyterLite Plugin
```yaml
- jupyterlite:
    enabled: true
    notebook_patterns:
      - "BC_Weeks/**/*.ipynb"
```

**What it does**: Embeds an interactive Jupyter notebook environment that runs entirely in the browser using WebAssembly (Pyodide).

**Why it's awesome**:
- Students can run Python code without installing anything
- No server required - runs in the browser
- Perfect for educational content

**Learn more**:
- [JupyterLite Docs](https://jupyterlite.readthedocs.io/)
- [mkdocs-jupyterlite Plugin](https://github.com/jupyterlite/mkdocs-jupyterlite)

---

### Section Index Plugin
```yaml
- section-index
```

**What it does**: Works with `navigation.indexes` to make section folder names clickable.

**Example**: Clicking "Home" in the sidebar takes you to the Home section's index page.

**Learn more**: [mkdocs-section-index](https://github.com/oprypin/mkdocs-section-index)

---

### GLightbox Plugin
```yaml
- glightbox
```

**What it does**: Creates a lightbox overlay when clicking on images - they pop up in a modal for better viewing.

**Try it**: Click any image in the documentation to see the effect.

**Learn more**: [mkdocs-glightbox](https://github.com/blueswen/mkdocs-glightbox)

## Markdown Extensions

### Code Highlighting

```yaml
- pymdownx.highlight:
    anchor_linenums: true
- pymdownx.inlinehilite
- pymdownx.snippets
- pymdownx.superfences
```

**What they do**:
- **highlight**: Syntax highlighting for code blocks with clickable line numbers
- **inlinehilite**: Highlight code inline like `this`
- **snippets**: Include external file snippets in your docs
- **superfences**: Advanced code block features (tabs, nested blocks)

**Learn more**: [PyMdown Extensions - Highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/)

---

### Admonitions (Callout Boxes)

```yaml
- admonition
- pymdownx.details
```

**What they do**: Create callout boxes for notes, warnings, tips, etc.

**Example**:
```markdown
!!! note "This is a note"
    Important information here!

!!! warning
    Be careful!
```

**Learn more**: [Admonitions Reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

---

### Content Tabs

```yaml
- pymdownx.tabbed:
    alternate_style: true
```

**What it does**: Creates tabbed content sections.

**Example**:
```markdown
=== "Python"
    ```python
    print("Hello")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hello")
    ```
```

**Learn more**: [Content Tabs Reference](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)

---

### Tables and TOC

```yaml
- tables
- toc:
    permalink: true
```

**What they do**:
- **tables**: Enhanced Markdown table support
- **toc**: Generates table of contents with permalink anchors (# symbols next to headings)

**Learn more**: [Python Markdown TOC](https://python-markdown.github.io/extensions/toc/)

## Theme Color Configuration

```yaml
palette:
  # Light mode
  - scheme: default
    primary: indigo
    accent: indigo
  # Dark mode
  - scheme: slate
    primary: indigo
    accent: indigo
```

**What it does**: Sets up dual theme with toggle button.

**Available colors**: red, pink, purple, indigo, blue, cyan, teal, green, lime, yellow, amber, orange, brown

**Learn more**: [Color Customization](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

## Navigation Structure

The `nav` section in `mkdocs.yml` defines the sidebar structure:

```yaml
nav:
  - Home:
    - index.md                          # First file = section landing page
    - Course Overview: home/course-overview.md
  - Getting Started:
    - getting-started/index.md
```

**Key points**:
- Indentation matters (YAML format)
- First item under a section = section index page
- Use descriptive titles followed by file paths
- Organize logically for user flow

**Learn more**: [Navigation Setup](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation)

## Local Development

### Serve the site locally
```bash
mkdocs serve
```
Opens at `http://127.0.0.1:8000/` with live reload - changes appear instantly.

### Build static files
```bash
mkdocs build
```
Creates HTML files in `site/` directory.

### Deploy to GitHub Pages
```bash
mkdocs gh-deploy
```
Builds and deploys to `gh-pages` branch.

**Learn more**: [Deploying Docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)

## Customization Tips

### Change the color scheme
Edit `theme.palette.primary` and `theme.palette.accent` in `mkdocs.yml`.

### Add a logo
```yaml
theme:
  logo: assets/logo.png
  favicon: assets/favicon.png
```

### Add custom CSS
Create `docs/stylesheets/extra.css`:
```yaml
extra_css:
  - stylesheets/extra.css
```

### Add Google Analytics
```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

**Learn more**: [Analytics Setup](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)

## Useful Resources

### Official Documentation
- [MkDocs](https://www.mkdocs.org/) - Core documentation
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Theme documentation
- [Material Reference](https://squidfunk.github.io/mkdocs-material/reference/) - All features

### Extensions
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/) - Markdown enhancements
- [MkDocs Plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) - Plugin catalog

### Interactive Features
- [JupyterLite](https://jupyterlite.readthedocs.io/) - Browser-based Jupyter
- [Pyodide](https://pyodide.org/) - Python in WebAssembly

## Troubleshooting

### Navigation not showing correctly?
- Check `mkdocs.yml` indentation (must be spaces, not tabs)
- Verify all file paths exist
- Ensure `navigation.indexes` is enabled

### Search not working?
- Rebuild the site: `mkdocs build --clean`
- Clear browser cache
- Check that `search` plugin is enabled

### JupyterLite not loading?
- Check console for errors (F12 in browser)
- Verify notebook paths in `notebook_patterns`
- Ensure JupyterLite plugin is properly installed

### Images not displaying?
- Use paths relative to markdown file location
- Or use absolute paths from `docs/` directory
- Check image file extensions are lowercase

---

**Related Guides**:
- [MkDocs Setup Guide](../guidelines/mkdocs-setup-guide.md) - Initial setup instructions
- [Clean Code Before PR](clean-code-before-pr.md) - Contribution guidelines

[← Back to Tutorials](index.md)
