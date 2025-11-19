Run comprehensive quality review for the current implementation

This command runs quality checks and verification following the project standards.

**Usage:**
- /quality-review [module_path]

**Examples:**
- /quality-review (reviews entire codebase)
- /quality-review src/auth/login.py (reviews specific module)

**Process:**

Follow .github/instructions/quality-checklists.md, .github/instructions/post-test-review.instructions.md, and optionally .github/prompts/verify-implementation.prompt.md for detailed module verification.

### 1. Automated Checks

Run all automated quality tools:

```bash
# Run all tests
pytest -v

# Check test coverage (must be ≥ 90%)
pytest --cov=src --cov-report=term --cov-report=html

# Run linter
ruff check src/ test/

# Apply formatting
ruff format src/ test/
```

### 2. Code Quality Review

- ✅ Docstrings follow docs/rules/docstring-standards.md
- ✅ Output format follows docs/rules/output-format.md
- ✅ Test structure mirrors src/ structure
- ✅ No TODO comments without tracking
- ✅ No debug print statements
- ✅ Proper error handling

### 3. Security Review

Follow .github/instructions/security-review.instructions.md:

- ✅ No hardcoded credentials
- ✅ CodeGuard rules applied
- ✅ Input validation present
- ✅ No sensitive data in logs
- ✅ Proper exception handling
- ✅ Threat model mitigations implemented

### 4. Documentation Review

- ✅ docs/SPEC-CROSS-REFERENCE.md updated
- ✅ docs/INDEX.md updated
- ✅ All code has ABOUTME comments
- ✅ README files updated if needed

### 5. Detailed Module Verification (Optional)

For comprehensive module-level verification, use the verify-implementation prompt:

```
Use the verify-implementation prompt for {module_path}
```

This provides detailed analysis including:
- Import validation
- Type checking (if configured)
- Test structure and quality
- Platform independence
- Integration verification
- Comprehensive pass/fail reporting

See .github/prompts/verify-implementation.prompt.md for details.

### 6. Generate Report

Create quality report with:
- Test results (count, pass/fail, coverage %)
- Ruff check results
- Security review findings
- Documentation completeness
- Overall PASS/FAIL status
- Issues found and recommendations

**Expected Output:**
- Quality report in terminal
- Coverage report: htmlcov/index.html
- List of any issues to fix

**Next Step:** Fix any issues found, or proceed to human approval if all checks pass