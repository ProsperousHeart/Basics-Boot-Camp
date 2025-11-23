# Workflow Prompt: Specification → Code (TDD Complete)

**Purpose**: Orchestrate the complete workflow from specification to tested, reviewed code
**Input**: Specification document path
**Output**: Source code, tests, quality reports, updated documentation
**References**: Multiple prompts and instructions

## 🔄 Workflow Overview

This prompt orchestrates the complete Specification → Code workflow including:

1. TDD code generation (RED-GREEN-REFACTOR cycles)
2. Security review
3. Quality validation
4. Post-test review
5. Documentation updates

## 📋 Master Orchestration Prompt

```
I need you to execute the complete Specification → Code workflow for the specification at {specification_path} using Test-Driven Development.

Follow these steps in order:

### Step 1: Review Specification and Create Test Plan

Read {specification_path} thoroughly and identify:
- All functions/classes to implement
- Test scenarios from acceptance criteria
- Relevant CodeGuard files needed
- Integration points
- Data structures required

**Create comprehensive test plan** for each function/class:
- Functional tests (expected behaviors)
- Security tests (input validation, injection prevention, auth/authz)
- Edge case tests
- Error condition tests

**Present test plan to user** in structured format:
```
Test Plan for {module_name}:

Function: {function_name}
- Functional Tests:
  - test_{behavior}: {description}
- Security Tests:
  - test_{security_aspect}: {description}
- Edge Cases:
  - test_{edge_case}: {description}
```

**⚠️ APPROVAL GATE: Wait for user approval before proceeding to Step 2.**

User may request:
- Additional tests
- Removal of unnecessary tests
- Modification of test scope
- Clarification of test objectives

### Step 2: TDD Implementation with Shift-Left Security

**IMPORTANT**: Only proceed after user approves test plan from Step 1.

**Security is not a phase - it's continuous practice in every TDD cycle.**

Use the prompt at .github/prompts/generate-code-from-spec.prompt.md for {specification_path}.

Follow the TDD workflow at .github/instructions/tdd-workflow.instructions.md strictly:

For EACH function/method:
1. 🔴 RED: Write failing tests
   - Write functional test (standard behavior)
   - Verify it fails for the right reason
   - **BEFORE implementing, add security tests:**
     - Input validation (boundary, type, format, null handling)
     - Injection prevention (XSS, SQL, command, path traversal)
     - Authentication/authorization (permissions, roles)
   - Verify ALL tests fail
   - Report: Tests written (functional + security)
2. 🟢 GREEN: Write code to pass ALL tests
   - Implement code passing BOTH functional AND security tests
   - **Use secure coding practices** (whitelist validation, parameterized queries, fail securely, etc.)
   - Run all tests, verify ALL pass
   - Report: Code added, all tests passing, secure practices applied
3. 🔵 REFACTOR: Improve while maintaining security
   - Refactor code keeping ALL tests green
   - **Never sacrifice security for elegance**
   - Report: Refactoring done, security maintained

Document each RED-GREEN-REFACTOR cycle in the execution log, including security measures applied.

Wait for all implementation to complete before proceeding.

### Step 3: Final Security Review

**Note**: Security should have been integrated throughout TDD cycles. This step is final verification and gap filling.

Conduct comprehensive security review following .github/instructions/security-review.instructions.md including:
- ✅ CodeGuard compliance verification (should already be applied)
- ✅ Threat model mitigation implementation check
- ✅ Security test case validation (should already pass)
- ✅ No hardcoded credentials
- ✅ Proper error handling (no sensitive data leakage)
- ✅ Input validation present (should be in place)
- ✅ Logging doesn't capture PII

**If security gaps found**: Fix immediately and re-run TDD cycles for affected code.

Report security findings (if any).

### Step 4: Quality Validation

Conduct code generation stage quality review following .github/instructions/quality-checklists.md (Code Generation Stage section).

Run automated checks:
- ✅ `pytest -v` - All tests pass
- ✅ `pytest --cov=src --cov-report=term` - Coverage ≥ 90%
- ✅ `ruff check src/ test/` - Linting passes
- ✅ `ruff format src/ test/` - Formatting applied

Report results:
- ✅ Items that pass
- ❌ Items that fail (with details)
- 🟡 Items that need attention

### Step 5: Implementation Verification (Optional but Recommended)

For critical or complex modules, run detailed verification using .github/prompts/verify-implementation.prompt.md.

This provides comprehensive analysis including:
- Import validation
- Type checking (if configured)
- Test structure and quality verification
- Platform independence checks
- Integration verification
- Detailed pass/fail reporting

### Step 6: Post-Test Review

Conduct post-test review following .github/instructions/post-test-review.instructions.md.

Verify:
- ✅ All tests pass with pristine output
- ✅ Test coverage ≥ 90%
- ✅ Ruff checks and formatting pass
- ✅ Documentation standards followed
- ✅ Cross-reference table updated
- ✅ No TODO comments without tracking
- ✅ Platform independence verified
- ✅ Security review passed
- ✅ Test quality is high

### Step 7: Documentation Update

Verify the following are updated:
- docs/SPEC-CROSS-REFERENCE.md (source and test files added)
- docs/specifications/spec_{name}.md (implementation status updated)
- Source code docstrings (following docs/rules/docstring-standards.md)
- docs/rules/error-resolution-kb.md (if errors were self-fixed)

### Step 8: Create Execution Log

Create an execution log following docs/rules/output-format.md in .github/prompts/output-logs/{timestamp}-code-workflow.md including:
- All TDD cycles documented (RED-GREEN-REFACTOR for each feature)
- CodeGuard files applied and why
- Test results at each stage
- Security review results
- Quality check results
- Issues encountered and resolutions
- Files created/updated
- Next steps

### Step 9: Report Summary

Provide a summary including:
- ✅ Success status
- 📁 Files created (source + tests)
- 🔒 CodeGuard rules applied
- 🧪 Test results (count, coverage %)
- 📋 Quality review results
- 🔒 Security review results
- ⏳ Next step: Human review and approval

If quality or security review fails (❌), stop and request fixes before proceeding.
```

## 💡 Usage Examples

### With Claude Code

```
Execute the workflow-spec-to-code prompt for docs/specifications/spec_user-auth.md
```

### With GitHub Copilot

```
@workspace Implement @docs/specifications/spec_user-auth.md using TDD following the workflow at @.github/prompts/workflow-spec-to-code.prompt.md. Include security review and quality validation.
```

### Manual Step-by-Step

If you prefer to execute each step individually:

```
# Step 1
Review docs/specifications/spec_user-auth.md

# Step 2
Implement using TDD (RED-GREEN-REFACTOR for each feature)

# Step 3
Conduct security review using security-review.instructions.md

# Step 4
Run quality checks: pytest, coverage, ruff
Conduct quality review using quality-checklists.md

# Step 5 (Optional but Recommended)
Run detailed verification using verify-implementation.prompt.md

# Step 6
Conduct post-test review using post-test-review.instructions.md

# Step 7
Verify documentation updates

# Step 8
Create execution log

# Step 9
Report summary
```

## 🚦 Decision Points

### TDD Granularity

Decide how to break down implementation:

- **Function-by-function**: RED-GREEN-REFACTOR for each function
- **Feature-by-feature**: RED-GREEN-REFACTOR for complete features
- **Class-by-class**: RED-GREEN-REFACTOR for entire classes

Recommendation: Function-by-function for better test quality

### Test Coverage Threshold

Default: 90% coverage required

Adjust if:

- Security-critical code: 100% required
- Simple utilities: 80% acceptable
- UI/presentation layer: Lower threshold OK

### Security Review Failure

If security issues found:

1. AI should attempt fixes using CodeGuard guidelines
2. Re-run security review
3. Document in error KB if pattern is common
4. Request human guidance for complex issues

### Quality Review Failure

If quality issues found:

1. Fix automated issues (ruff, formatting)
2. Improve docstrings to meet standards
3. Add missing tests
4. Re-run quality checks
5. Request human guidance if stuck

### Approval Gate

After workflow completes:

- Human reviews generated code and tests
- Runs code locally to verify
- Reviews quality and security reports
- If approved → Merge/deploy
- If rejected → Document feedback, make corrections

## 📊 Expected Output

After successful completion:

```
✅ Specification → Code Workflow Complete

📁 Files Created:
- src/auth/login.py
- src/auth/session.py
- test/test_auth/test_login.py
- test/test_auth/test_session.py
- .github/prompts/output-logs/2025-11-09-153045-code-workflow.md

📝 Files Updated:
- docs/SPEC-CROSS-REFERENCE.md
- docs/specifications/spec_user-auth.md
- docs/rules/error-resolution-kb.md (added requests.Timeout handling)

🧪 Test Results:
- Total tests: 24
- Passed: 24
- Failed: 0
- Coverage: 94%

🔒 CodeGuard Files Applied:
- codeguard-0-authentication-mfa.instructions.md
  - MFA support implemented
  - Password hashing with bcrypt
- codeguard-0-input-validation-injection.instructions.md
  - Email validation
  - SQL injection prevention with parameterized queries
- codeguard-0-session-management-and-cookies.instructions.md
  - Secure cookie flags set
  - Session timeout implemented

📋 Quality Review: ✅ PASSED
- All TDD cycles completed
- All tests green
- Ruff checks pass
- Docstrings meet standards
- Code coverage exceeds threshold

🔒 Security Review: ✅ PASSED
- No hardcoded credentials
- All CodeGuard recommendations followed
- Threat model mitigations implemented
- Security test cases pass

⏳ Next Step: Human code review and approval
```

## 🔧 Troubleshooting

### Tests Keep Failing

1. Review test expectations - are they correct?
2. Check implementation logic
3. Add debug logging temporarily
4. Break down into smaller functions
5. Request human guidance

### Low Test Coverage

1. Identify uncovered lines: `pytest --cov=src --cov-report=html`
2. Add tests for missing scenarios
3. Focus on error paths and edge cases

### CodeGuard Compliance Issues

1. Review specific CodeGuard file for guidance
2. Check error KB for similar issues
3. Apply recommended patterns
4. Re-run security review

### Ruff Errors

1. Run `ruff check src/ test/` to see issues
2. Auto-fix where possible: `ruff check --fix src/ test/`
3. Apply formatting: `ruff format src/ test/`
4. Fix remaining issues manually

## 🔗 Related Documentation

- [Master Workflow](../.github/instructions/master-workflow.md)
- [TDD Workflow](../.github/instructions/tdd-workflow.instructions.md)
- [Generate Code Prompt](generate-code-from-spec.prompt.md)
- [Security Review](../.github/instructions/security-review.instructions.md)
- [Quality Checklists](../.github/instructions/quality-checklists.md)
- [Post-Test Review](../.github/instructions/post-test-review.instructions.md)
- [Output Format](../../docs/rules/output-format.md)

---

**TODO**: Add examples of complex TDD scenarios and handling integration tests
