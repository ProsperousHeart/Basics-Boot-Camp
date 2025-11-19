Execute the comprehensive verification prompt at `.github/prompts/verify-implementation.prompt.md` for module: {{$1}}

This command runs comprehensive verification of a Python module implementation.

**Usage:**

```
/verify src/auth/login.py
/verify src/utils/
```

**What it does:**

1. **Import Validation**: Checks all imports are valid and dependencies declared
2. **Type Checking**: Verifies type hints if mypy/pyright configured
3. **Test Structure**: Verifies tests exist, are high quality, and follow AAA pattern
4. **Test Execution**: Runs pytest and checks coverage (≥ 90%)
5. **Code Quality**: Runs ruff linting and formatting checks
6. **Documentation**: Verifies ABOUTME comments, docstrings, and type hints
7. **Security**: Checks for hardcoded secrets, CodeGuard compliance
8. **Platform Independence**: Verifies path handling and test isolation
9. **UI/Accessibility**: Checks HTML, CSS, and a11y if UI components exist
10. **Integration**: Verifies module imports and integrations work

**Output:**

- Comprehensive pass/fail report
- Specific issues with line numbers
- Recommendations for improvement
- Overall PASS/FAIL verdict

**Report Sections:**

- ✅ Import Validation
- ✅ Type Checking (if applicable)
- ✅ Test Results (with coverage)
- ✅ Code Quality (ruff)
- ✅ Documentation (docstrings, ABOUTME)
- ✅ Security (no secrets, CodeGuard)
- ✅ Platform Independence
- ✅ UI/CSS/Accessibility (if applicable)
- ✅ Integration

**Next Steps:**

- If PASS: Ready for human review
- If FAIL: Address issues and re-verify

**Note:** This command delegates to the tool-agnostic prompt at `.github/prompts/verify-implementation.prompt.md`