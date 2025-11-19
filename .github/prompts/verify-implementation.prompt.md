# Prompt: Verify Implementation

**Purpose**: Comprehensive verification of Python code implementation
**Input**: Module/package path to verify
**Output**: Detailed verification report with pass/fail status
**References**:

- `.github/instructions/quality-checklists.md`
- `.github/instructions/post-test-review.instructions.md`
- `docs/rules/docstring-standards.md`

## Prompt

```
You are verifying the implementation at: {module_path}

Perform comprehensive implementation verification following these steps:

## Step 1: Pre-flight Validation

1. **Check module/package exists**:
   - Verify the file/directory exists at `src/{module_path}`
   - If file doesn't exist, report error and suggest available modules in `src/`
   - List the module structure if it's a package

2. **Read implementation files**:
   - Read all source files in the module
   - Extract module/class/function names
   - Identify public API (functions/classes without leading underscore)

3. **Validate imports**:
   - Check all import statements are valid
   - Verify internal imports use correct paths and platform independent syntax
   - Confirm required dependencies are in requirements.txt
   - Check for unused imports
   - Verify data model imports where applicable

## Step 2: Python Type Checking (if applicable)

1. **Check for type hints**:
   - Verify function signatures have type hints
   - Check return types are annotated
   - Verify complex types use proper typing imports (List, Dict, Optional, etc.)
   - Report missing type hints

2. **Run type checker** (if mypy or pyright configured):
   - Execute type checking tool
   - Report all type errors with line numbers
   - Identify which errors relate to the module being verified
   - Fix missing or inaccurate types if possible

3. **Verify type accuracy**:
   - Check types match actual usage
   - Confirm Optional is used for nullable values
   - Verify generic types are properly parameterized

## Step 3: Test Structure Verification

1. **Verify test files exist**:
   - Check that `test/test_{module-name}.py` exists
   - Verify test directory mirrors `src/` structure
   - Confirm all public functions/classes have corresponding tests

2. **Check test quality**:
   - Verify tests use AAA pattern (Arrange, Act, Assert)
   - Check tests are independent (no shared state)
   - Confirm test names follow convention: `test_{behavior}_description`
   - Verify edge cases are tested
   - Check error conditions are tested
   - Ensure mocks/stubs are used appropriately for external dependencies
   - Confirm tests clean up any temporary files or state
   - Verify tests run quickly (no long sleeps or waits)
   - Check for proper use of fixtures for setup/teardown
   - Check for optimization opportunities (e.g., parameterized tests using the id argument)

3. **Run tests**:
   - Execute `pytest -v` for the module's tests
   - Report pass/fail status
   - Identify any failing tests
   - Check for skipped tests and verify justification
   - Test with mock data where applicable

4. **Verify test coverage**:
   - Run `pytest --cov={module_path} --cov-report=term`
   - Check coverage meets threshold (90%+)
   - Identify uncovered lines
   - Report coverage percentage

## Step 4: Code Quality Verification

1. **Run linting**:
   - Execute `ruff check src/{module_path} test/test_{module_name}.py`
   - Report all linting errors with line numbers
   - Auto-fix if possible: `ruff check --fix`
   - Report remaining issues

2. **Check formatting**:
   - Execute `ruff format --check src/{module_path} test/test_{module_name}.py`
   - Apply formatting if needed: `ruff format`
   - Confirm formatting compliance

3. **Verify code standards**:
   - Check no TODO comments without tracking issue
   - Verify no commented-out code
   - Confirm no debug print statements
   - Check proper error handling exists
   - Verify logging uses project logger (not print)

## Step 5: Documentation Verification

1. **Verify ABOUTME comments**:
   - Check all module files start with 2-line ABOUTME comment
   - Verify format: `ABOUTME: {description}`
   - Confirm description accurately describes the file

2. **Check docstrings**:
   - Verify module has module-level docstring
   - Check all public functions have docstrings
   - Verify all classes have docstrings
   - Confirm docstrings follow `docs/rules/docstring-standards.md` (Google style)
   - Check docstrings include:
     - Function/class description
     - Args with types and descriptions
     - Returns with type and description
     - Raises for exceptions
     - Examples for complex functions

3. **Verify type hints in signatures**:
   - Check all parameters have type annotations
   - Verify return types are annotated
   - Confirm complex types properly documented

## Step 6: Security Verification

1. **Check for security issues**:
   - Verify no hardcoded credentials or secrets
   - Check secrets loaded from environment variables
   - Confirm input validation implemented
   - Verify error messages don't leak sensitive data
   - Check logging doesn't capture PII or credentials

2. **Verify CodeGuard compliance**:
   - Identify relevant CodeGuard files for the module
   - Check CodeGuard recommendations are followed
   - Verify security test cases exist for sensitive operations
   - Confirm threat model mitigations implemented (if applicable)

3. **Run security checks** (if bandit configured):
   - Execute security linting
   - Report security warnings
   - Assess severity and fix critical issues

## Step 7: Platform Independence Verification

1. **Check path handling**:
   - Verify use of `pathlib.Path` or `os.path` (not hardcoded slashes)
   - Check no Windows-specific or Linux-specific code
   - Confirm environment variables handled correctly

2. **Verify test isolation**:
   - Check logger isolation pattern is used in tests
   - Verify temporary files/directories properly handled
   - Confirm tests don't depend on specific working directory

3. **Test on current platform**:
   - Run tests on current platform (Windows/Linux)
   - Verify no platform-specific failures
   - Check output is pristine (no warnings or errors)

## Step 8: UI/CSS/Accessibility Verification (if applicable)

**First, detect if the module has UI components:**
- Check for HTML templates (`.html`, `.jinja2`, `.j2` files)
- Look for CSS/styling files (`.css`, inline styles)
- Identify web framework usage (Flask, Django, FastAPI with Jinja2)
- Detect GUI frameworks (Tkinter, PyQt, Kivy)
- Find data visualization tools (Plotly, Dash, Streamlit)
- Check for CLI output formatting (Rich, Click styling)

**If UI components are detected, perform the following checks:**

### 8.1: HTML/Template Validation

1. **Validate HTML structure**:
   - Check for proper DOCTYPE declaration
   - Verify all tags are properly closed
   - Confirm proper nesting of elements
   - Check for valid HTML5 semantics
   - Verify no inline event handlers (use external JS)

2. **Template security**:
   - Verify template auto-escaping is enabled
   - Check no `|safe` filter on user input
   - Confirm CSP headers are set (if web app)
   - Verify CSRF protection enabled (if forms present)
   - Check for XSS vulnerabilities in template rendering

3. **Template best practices**:
   - Verify templates use inheritance/includes appropriately
   - Check for code duplication in templates
   - Confirm separation of concerns (no business logic in templates)
   - Verify template variables are properly documented

### 8.2: CSS/Styling Verification

1. **CSS organization**:
   - Verify CSS files are properly organized
   - Check for unused CSS selectors
   - Confirm no inline styles (except dynamically required)
   - Verify CSS follows project naming conventions (BEM, etc.)
   - Check for CSS framework compatibility (Bootstrap, Tailwind, etc.)

2. **Responsive design**:
   - Verify mobile-first approach (if applicable)
   - Check media queries for common breakpoints
   - Test layout doesn't break at various viewport sizes
   - Verify images are responsive and optimized

3. **CSS quality**:
   - Check for CSS validation errors
   - Verify no `!important` abuse
   - Confirm color contrast meets WCAG standards (see 8.3)
   - Check for CSS performance issues (excessive specificity, etc.)
   - Verify fallbacks for older browsers (if required)

### 8.3: Accessibility (a11y) Verification

1. **Semantic HTML**:
   - Verify proper heading hierarchy (h1 → h2 → h3, etc.)
   - Check for semantic elements (`<nav>`, `<main>`, `<article>`, `<aside>`)
   - Confirm landmarks are properly used
   - Verify no `<div>` soup (use semantic elements when appropriate)

2. **ARIA attributes**:
   - Check `aria-label` and `aria-labelledby` for non-text elements
   - Verify `role` attributes used appropriately
   - Confirm `aria-live` regions for dynamic content
   - Check `aria-hidden` doesn't hide interactive elements
   - Verify ARIA states updated dynamically (if interactive)

3. **Keyboard navigation**:
   - Verify all interactive elements are keyboard accessible
   - Check tab order is logical and sequential
   - Confirm focus indicators are visible (`:focus` styles)
   - Verify no keyboard traps
   - Test skip links for navigation bypass

4. **Color contrast**:
   - Verify text meets WCAG AA standards (4.5:1 for normal text, 3:1 for large)
   - Check color is not the only means of conveying information
   - Verify links are distinguishable from text (not just by color)
   - Test with color blindness simulators (if critical)

5. **Alternative text**:
   - Verify all images have `alt` attributes
   - Check `alt` text is descriptive (not "image" or filename)
   - Confirm decorative images use empty `alt=""`
   - Verify complex images have longer descriptions (`aria-describedby`)

6. **Forms accessibility**:
   - Verify all form inputs have associated `<label>` elements
   - Check for proper `for`/`id` association
   - Confirm error messages are announced to screen readers
   - Verify required fields indicated (not just visually)
   - Check form validation provides clear, accessible feedback

7. **CLI accessibility** (if CLI application):
   - Verify color output respects `NO_COLOR` environment variable
   - Check output works with screen readers
   - Confirm Unicode/emoji doesn't break in all terminals
   - Verify color contrast for terminal themes
   - Test with `--no-color` or `--plain` flags

### 8.4: Browser/Client Testing (if web application)

1. **Cross-browser compatibility**:
   - Test in Chrome/Edge (Chromium)
   - Test in Firefox
   - Test in Safari (if applicable)
   - Verify polyfills for older browsers (if required)

2. **Performance**:
   - Check page load times
   - Verify no blocking resources
   - Confirm lazy loading for images/assets
   - Check for memory leaks in client-side code
   - Verify no excessive repaints/reflows

3. **JavaScript verification** (if applicable):
   - Check for JavaScript errors in console
   - Verify progressive enhancement (site works without JS)
   - Confirm event listeners properly cleaned up
   - Test with JavaScript disabled

### 8.5: UI Testing

1. **Automated UI tests**:
   - Check for Selenium/Playwright tests (web apps)
   - Verify visual regression tests (if configured)
   - Confirm UI component tests exist
   - Check snapshot tests for UI components (if applicable)

2. **Manual UI verification**:
   - Test all interactive elements work as expected
   - Verify error states display correctly
   - Check loading states are user-friendly
   - Confirm success/feedback messages appear
   - Verify modals/dialogs can be closed

3. **Accessibility testing tools**:
   - Run axe-core or similar a11y checker (if web app)
   - Check WAVE browser extension results
   - Verify Lighthouse accessibility score (if web app)
   - Test with screen reader (NVDA, JAWS, VoiceOver)

**If no UI components detected, skip to Step 9.**

## Step 9: Integration Verification

1. **Verify module can be imported**:
   - Check imports work: `python -c "import src.{module_path}"`
   - Verify public API is accessible
   - Confirm no import-time errors

2. **Check integration points**:
   - Verify module integrates with existing codebase
   - Check no breaking changes introduced
   - Confirm dependencies are compatible

3. **Test with realistic data** (if applicable):
   - Verify module handles expected data formats
   - Check edge cases (empty data, large data, malformed data)
   - Confirm graceful error handling

## Step 10: Generate Verification Report

Create a comprehensive pass/fail report with the following sections:

### Verification Summary
- ✅ PASS or ❌ FAIL for overall verification
- Module name and file path(s)
- Timestamp of verification
- Python version used

### Import Validation
- ✅ PASS or ❌ FAIL
- List any import errors
- Note unused imports
- Verify dependency declarations

### Type Checking Results (if applicable)
- ✅ PASS or ❌ FAIL or ⚠️ NOT CONFIGURED
- List any type errors with line numbers
- Note missing type hints
- Report type accuracy issues

### Test Results
- ✅ PASS or ❌ FAIL
- Total tests: X
- Passed: X
- Failed: X (with details)
- Skipped: X (with justification)
- Coverage: X%
- Uncovered lines: [list if < 90%]

### Code Quality
- ✅ PASS or ❌ FAIL
- Ruff linting: ✅ PASS or ❌ FAIL
- Ruff formatting: ✅ PASS or ❌ FAIL
- Code standards: ✅ PASS or ❌ FAIL
- Issues found: [list with line numbers]

### Documentation
- ✅ PASS or ❌ FAIL
- ABOUTME comments: ✅ PASS or ❌ FAIL
- Module docstring: ✅ PASS or ❌ FAIL
- Function docstrings: ✅ PASS or ❌ FAIL (X/Y functions documented)
- Class docstrings: ✅ PASS or ❌ FAIL (X/Y classes documented)
- Docstring quality: ✅ PASS or ❌ FAIL
- Type hints: ✅ PASS or ❌ FAIL

### Security
- ✅ PASS or ❌ FAIL
- No hardcoded secrets: ✅ PASS or ❌ FAIL
- Input validation: ✅ PASS or ❌ FAIL or ⚠️ N/A
- CodeGuard compliance: ✅ PASS or ❌ FAIL
- CodeGuard files referenced: [list]
- Security warnings: [list if any]

### Platform Independence
- ✅ PASS or ❌ FAIL
- Path handling: ✅ PASS or ❌ FAIL
- Test isolation: ✅ PASS or ❌ FAIL
- Platform compatibility: ✅ PASS or ❌ FAIL

### UI/CSS/Accessibility (if applicable)
- ✅ PASS or ❌ FAIL or ⚠️ N/A (no UI components)
- HTML/Template validation: ✅ PASS or ❌ FAIL or ⚠️ N/A
- CSS/Styling: ✅ PASS or ❌ FAIL or ⚠️ N/A
- Accessibility (a11y): ✅ PASS or ❌ FAIL or ⚠️ N/A
  - Semantic HTML: ✅ PASS or ❌ FAIL
  - ARIA attributes: ✅ PASS or ❌ FAIL
  - Keyboard navigation: ✅ PASS or ❌ FAIL
  - Color contrast (WCAG AA): ✅ PASS or ❌ FAIL
  - Alternative text: ✅ PASS or ❌ FAIL
  - Forms accessibility: ✅ PASS or ❌ FAIL
- Browser compatibility: ✅ PASS or ❌ FAIL or ⚠️ N/A
- UI tests: ✅ PASS or ❌ FAIL or ⚠️ N/A
- Accessibility testing tools: [list tools used and scores]
- Issues found: [list with line numbers/templates]

### Integration
- ✅ PASS or ❌ FAIL
- Import successful: ✅ PASS or ❌ FAIL
- Integration points: ✅ PASS or ❌ FAIL
- No breaking changes: ✅ PASS or ❌ FAIL

### Specific Issues Found

List each issue with:
- 🔴 **Critical**: Blocks functionality, security risk, or test failures
- 🟡 **Warning**: Quality issue, missing documentation, or low coverage
- 🔵 **Info**: Suggestions for improvement

Format:
- **Severity**: {issue description}
  - Location: `{file}:{line}`
  - Fix: {suggested fix}

### Recommendations

- List suggestions for improvement
- Note best practices that could be applied
- Suggest performance optimizations if applicable
- Recommend additional tests for edge cases

### Overall Status

**VERDICT**: ✅ PASS or ❌ FAIL

**Summary**: {brief summary of verification results}

**Next Steps**:
- If PASS: Ready for human review
- If FAIL: Address issues listed above and re-verify
```

## Important Guidelines

- **Be thorough**: Check every aspect of the implementation systematically
- **Be specific**: Provide exact line numbers and file paths for issues
- **Be helpful**: Offer concrete suggestions for fixing issues
- **Fix what you can**: Auto-fix formatting, linting, and clear issues
- **Don't break working code**: Only make changes that improve quality or fix clear bugs
- **Test thoroughly**: Verify implementation works with expected data
- **Consider context**: Some checks may not apply to all module types

## Error Handling

- If module doesn't exist, list available modules in `src/`
- If tests fail completely, show full error output
- If imports fail, investigate and report why
- If coverage is low, identify specific uncovered scenarios

## Example Usage

### With Claude Code

```
Use the verify-implementation prompt for src/auth/login.py
```

### With GitHub Copilot

```
@workspace Verify the implementation at @src/auth/login.py following @.github/prompts/verify-implementation.prompt.md. Generate a comprehensive verification report.
```

### As part of workflow

```
After TDD implementation completes, verify the code using verify-implementation prompt before final review.
```

## Expected Output

A detailed verification report showing:
- Overall PASS/FAIL status
- Results for each verification category
- Specific issues with locations and suggested fixes
- Recommendations for improvement
- Next steps based on results

---

**Related Documentation**:
- [Quality Checklists](../.github/instructions/quality-checklists.md)
- [Post-Test Review](../.github/instructions/post-test-review.instructions.md)
- [Docstring Standards](../../docs/rules/docstring-standards.md)
- [TDD Workflow](../.github/instructions/tdd-workflow.instructions.md)