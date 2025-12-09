# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2025-12-05]

### Added
- **JupyterLite Documentation Enhancements**
  - Added detailed technical explanation for why JupyterLite opens in a new tab instead of being embedded
  - Added comprehensive notebook reset instructions with 4 different methods:
    - Reset individual notebooks via File → Revert or delete/refresh
    - Clear all JupyterLite data via Settings → Advanced Settings Editor
    - Clear browser storage with browser-specific instructions (Chrome/Edge/Firefox)
    - Download fresh copy from GitHub repository
  - Added security attributes (`target="_blank"` and `rel="noopener noreferrer"`) to all JupyterLite launch links
  - Added visual indicator "(Opens in New Tab)" to launch buttons

### Changed
- **Navigation Structure**
  - Updated `mkdocs.yml` navigation to point "Interactive Notebooks" to landing page (`interactive-jupyter.md`) instead of directly to JupyterLite
  - Improved user experience by providing context and instructions before launching interactive environment

### Technical Details
- **Files Modified:**
  - `docs/interactive-jupyter.md` - Enhanced documentation
  - `mkdocs.yml` - Updated navigation (line 98)

- **Why These Changes:**
  - Addressed user confusion about notebook state persistence across server restarts
  - Explained browser storage behavior and JupyterLite architecture
  - Documented technical limitations preventing iframe embedding (Service Workers, CORS/CSP, URL routing)
  - Improved security with proper link attributes

---

## Template for Future Entries

```markdown
## [YYYY-MM-DD]

### Added
- New features or files added

### Changed
- Changes to existing functionality

### Deprecated
- Features that will be removed in upcoming releases

### Removed
- Features or files that have been removed

### Fixed
- Bug fixes

### Security
- Security improvements or vulnerability fixes

### Technical Details
- Implementation notes, file paths, or other technical information
```
