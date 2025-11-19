# Post-Test Review Instructions

**Last Updated**: 2025-11-09

Comprehensive quality review process after test execution, before human approval.

## 🎯 Purpose

This review ensures code quality, security, and completeness before human approval. It serves as the final quality gate in the TDD workflow.

## 📋 Review Process

### Step 1: Automated Test Validation

Run and verify all automated tests:

```bash
# Run all tests with verbose output
pytest -v

# Check test coverage (must be ≥ 90%)
pytest --cov=src --cov-report=term --cov-report=html

# Review coverage report
# Open htmlcov/index.html to see detailed coverage
```

**Checklist:**
- [ ] All tests pass
- [ ] No skipped tests without justification
- [ ] Test coverage meets threshold (90%+)
- [ ] No flaky tests (run tests multiple times if suspicious)
- [ ] Test output is pristine (no warnings or unexpected output)

**If tests fail:**
- Investigate root cause
- Fix implementation or test as appropriate
- Re-run tests until all pass
- Document any complex fixes in error KB

**If coverage is low:**
- Identify uncovered lines using coverage report
- Add tests for missing scenarios
- Focus on edge cases and error paths
- Re-run coverage check

### Step 2: Static Analysis and Code Quality

Run linting and formatting tools:

```bash
# Run linter
ruff check src/ test/

# Auto-fix linting issues where possible
ruff check --fix src/ test/

# Check formatting
ruff format --check src/ test/

# Apply formatting
ruff format src/ test/
```

**Checklist:**
- [ ] Ruff checks pass (no linting errors)
- [ ] Ruff formatting applied
- [ ] No TODO comments without tracking issue
- [ ] No commented-out code
- [ ] No debug print statements (use logging instead)
- [ ] Proper error handling throughout
- [ ] Logging uses project logger (not print)

**Common issues to fix:**
- Unused imports → Remove them
- Line too long → Refactor or break lines
- Missing docstrings → Add them
- Undefined names → Fix imports or typos

### Step 3: Documentation Review

Verify all documentation is complete and accurate:

**Code Documentation:**
- [ ] All modules have ABOUTME comments (2 lines at top)
- [ ] Module-level docstrings present
- [ ] All public functions have docstrings
- [ ] All classes have docstrings
- [ ] Docstrings follow `docs/rules/docstring-standards.md` (Google style)
- [ ] Type hints in all function signatures
- [ ] Complex functions include examples in docstrings

**Project Documentation:**
- [ ] `docs/SPEC-CROSS-REFERENCE.md` updated with source and test files
- [ ] `docs/INDEX.md` updated if new modules added
- [ ] README files updated if functionality changed
- [ ] Architecture diagrams updated if structure changed
- [ ] Execution log created in `docs/output-logs/` or `.github/prompts/output-logs/`

**Common issues to fix:**
- Missing ABOUTME → Add 2-line description
- Incomplete docstrings → Add Args, Returns, Raises
- Outdated cross-reference → Update with new files
- Missing examples → Add for complex functions

### Step 4: Security Review

Follow `.github/instructions/security-review.instructions.md`:

**Checklist:**
- [ ] No hardcoded credentials or secrets
- [ ] Secrets loaded from environment variables
- [ ] CodeGuard rules applied and documented
- [ ] Input validation present where needed
- [ ] Error messages don't leak sensitive data
- [ ] Logging doesn't capture PII or credentials
- [ ] Proper exception handling (no bare excepts)
- [ ] Threat model mitigations implemented (if applicable)
- [ ] Security test cases pass

**CodeGuard Verification:**
- Identify relevant CodeGuard files for the implementation
- Verify recommendations followed
- Document which CodeGuard files were applied and why
- Add security test cases for sensitive operations

**Common security issues to fix:**
- Hardcoded secrets → Move to environment variables
- Missing input validation → Add validation logic
- Sensitive data in logs → Sanitize or redact
- Broad exception handling → Make specific

### Step 5: Platform Independence Verification

Ensure code works across platforms (Windows/Linux/macOS):

**Checklist:**
- [ ] Path handling uses `pathlib.Path` or `os.path` (not hardcoded slashes)
- [ ] No platform-specific code without guards
- [ ] Environment variables handled correctly
- [ ] Test isolation pattern used (logger isolation)
- [ ] Temporary files/directories properly handled
- [ ] Tests don't depend on specific working directory
- [ ] Tests pass on current platform without warnings

**Common platform issues to fix:**
- Hardcoded paths with `\` or `/` → Use `pathlib.Path`
- Platform-specific commands → Use platform-agnostic libraries
- Encoding issues → Specify UTF-8 explicitly

### Step 6: Integration and Compatibility

Verify code integrates properly with the existing codebase:

**Checklist:**
- [ ] Module can be imported successfully
- [ ] Public API is accessible
- [ ] No import-time errors or warnings
- [ ] No breaking changes (or documented if necessary)
- [ ] Dependencies compatible with existing code
- [ ] Integration points verified and working
- [ ] Backward compatibility maintained (or breaking changes documented)


**Test integration:**

```bash
# Test import
python -c "import src.{module_path}"

# Run all project tests to verify no regressions
pytest -v
```

### Step 7: Module-Level Verification (Optional)

For critical or complex modules, run detailed verification:

```
Use the verify-implementation prompt for {module_path}
```

This provides comprehensive analysis including:
- Import validation
- Type checking (if configured)
- Test structure and quality verification
- Detailed pass/fail reporting

See `.github/prompts/verify-implementation.prompt.md` for details.

### Step 8: Generate Review Report

Create a post-test review report with:

```markdown
## Post-Test Review Report

**Date**: {timestamp}
**Module(s)**: {list of modules reviewed}
**Reviewer**: AI Assistant

### Test Results
- Total tests: X
- Passed: X
- Failed: 0
- Skipped: 0
- Coverage: X%
- **Status**: ✅ PASS

### Code Quality
- Ruff linting: ✅ PASS
- Ruff formatting: ✅ PASS
- Code standards: ✅ PASS
- **Status**: ✅ PASS

### Documentation
- Code documentation: ✅ PASS (X/X functions documented)
- Project documentation: ✅ PASS
- Cross-reference updated: ✅ YES
- **Status**: ✅ PASS

### Security
- CodeGuard compliance: ✅ PASS
- Security review: ✅ PASS
- CodeGuard files applied:
  - {list of CodeGuard files and rationale}
- **Status**: ✅ PASS

### Platform Independence
- Path handling: ✅ PASS
- Test isolation: ✅ PASS
- Platform compatibility: ✅ PASS
- **Status**: ✅ PASS

### Integration
- Import successful: ✅ PASS
- No regressions: ✅ PASS
- Integration verified: ✅ PASS
- **Status**: ✅ PASS

### Overall Status

**VERDICT**: ✅ PASS / ❌ FAIL

**Summary**: {brief summary of review results}

**Issues Found**: {count}
- 🔴 Critical: {count}
- 🟡 Warning: {count}
- 🔵 Info: {count}

**Issues Details**:
{list issues if any}

**Next Steps**:
- If PASS: Ready for human review and approval
- If FAIL: Address issues and re-run review
```

## 🚦 Pass/Fail Criteria

### PASS Criteria
All of the following must be true:
- ✅ All tests pass
- ✅ Coverage ≥ 90%
- ✅ Ruff checks pass
- ✅ All code documented
- ✅ Security review passed
- ✅ No critical issues

### FAIL Criteria
Any of the following results in FAIL:
- ❌ Any test fails
- ❌ Coverage < 80%
- ❌ Ruff errors present
- ❌ Missing documentation
- ❌ Security issues found
- ❌ Critical issues present

## 🔧 Common Issues and Fixes

### Issue: Tests Failing
**Fix**:
- Review test output for error details
- Check implementation logic
- Verify test expectations are correct
- Add debug logging if needed
- Fix implementation or test as appropriate

### Issue: Low Coverage
**Fix**:
- Run `pytest --cov=src --cov-report=html`
- Open `htmlcov/index.html` to see uncovered lines
- Add tests for uncovered scenarios
- Focus on edge cases and error paths

### Issue: Ruff Errors
**Fix**:
- Run `ruff check --fix src/ test/` to auto-fix
- Manually fix remaining issues
- Apply formatting with `ruff format src/ test/`

### Issue: Missing Documentation
**Fix**:
- Add ABOUTME comments to module files
- Add docstrings following Google style
- Include Args, Returns, Raises sections
- Add examples for complex functions

### Issue: Security Concerns
**Fix**:
- Move hardcoded secrets to environment variables
- Add input validation
- Sanitize error messages
- Follow relevant CodeGuard guidelines

## 📚 Related Documentation

- [Quality Checklists](quality-checklists.md) - Quality Stage section
- [Security Review](security-review.instructions.md)
- [Docstring Standards](../../docs/rules/docstring-standards.md)
- [TDD Workflow](tdd-workflow.instructions.md)
- [Verify Implementation Prompt](../.github/prompts/verify-implementation.prompt.md)
- [Output Format](../../docs/rules/output-format.md)

---

**Version**: 2.0
**Last Expanded**: 2025-11-09
