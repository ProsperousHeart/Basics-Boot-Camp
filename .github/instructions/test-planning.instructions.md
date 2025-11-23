# Test Planning Instructions

**Last Updated**: 2025-11-09

Guidelines for creating comprehensive test plans before TDD implementation.

## 🎯 Purpose

Test planning ensures:
- Comprehensive coverage of all requirements
- Security considerations are identified upfront
- Edge cases are not overlooked
- User has visibility and control over test scope
- Implementation is guided by clear objectives

## ⚠️ Approval Gate

**CRITICAL**: Test plans must be approved by the user before beginning TDD implementation.

This prevents:
- Wasted effort on unnecessary tests
- Missing critical test scenarios
- Security gaps in testing
- Misalignment with requirements

## 📋 Test Plan Structure

For each function/class to be implemented, create a test plan with these categories:

### 1. Functional Tests

Tests that verify expected behavior from the specification.

**Format:**
```
- test_{behavior_name}: {description of what behavior is verified}
```

**Example:**
```
Function: validate_email(email: str) -> bool

- Functional Tests:
  - test_validate_email_with_valid_input: Verify valid emails are accepted
  - test_validate_email_with_invalid_format: Verify invalid formats are rejected
  - test_validate_email_returns_boolean: Verify function returns bool type
```

### 2. Security Tests

Tests that verify security requirements and prevent vulnerabilities.

**Categories:**
- Input validation (type checking, boundary conditions, format validation)
- Injection prevention (XSS, SQL, command, path traversal)
- Authentication/Authorization (permission checks, role validation)
- Cryptographic operations (algorithm usage, key management)
- Sensitive data handling (no leakage in logs/errors)

**Format:**
```
- Security Tests:
  - test_{security_aspect}: {description of security verification}
```

**Example:**
```
Function: validate_email(email: str) -> bool

- Security Tests:
  - test_validate_email_type_validation: Verify non-string inputs are handled safely
  - test_validate_email_injection_prevention: Verify XSS payloads are rejected
  - test_validate_email_length_limits: Verify DoS prevention via length limits
  - test_validate_email_special_characters: Verify dangerous characters are rejected
```

### 3. Edge Case Tests

Tests for boundary conditions and uncommon scenarios.

**Format:**
```
- Edge Cases:
  - test_{edge_case}: {description of edge case scenario}
```

**Example:**
```
Function: validate_email(email: str) -> bool

- Edge Cases:
  - test_validate_email_empty_string: Verify empty string is handled
  - test_validate_email_whitespace_only: Verify whitespace-only input is handled
  - test_validate_email_maximum_length: Verify RFC 5321 max length (254 chars)
  - test_validate_email_unicode_characters: Verify unicode handling
```

### 4. Error Condition Tests

Tests for error handling and failure scenarios.

**Format:**
```
- Error Conditions:
  - test_{error_condition}: {description of error handling}
```

**Example:**
```
Function: get_user_by_id(user_id: int) -> User

- Error Conditions:
  - test_get_user_by_id_not_found: Verify returns None when user doesn't exist
  - test_get_user_by_id_database_error: Verify handles database connection errors
  - test_get_user_by_id_invalid_id_type: Verify raises TypeError for non-int ID
```

## 📝 Complete Test Plan Example

```markdown
## Test Plan for User Authentication Module

### Function: hash_password(password: str) -> str

#### Functional Tests:
- test_hash_password_returns_hash: Verify function returns hashed string
- test_hash_password_different_for_same_input: Verify salt makes hashes unique
- test_hash_password_verify_with_bcrypt: Verify hash can be verified with bcrypt

#### Security Tests:
- test_hash_password_uses_bcrypt: Verify uses bcrypt algorithm (starts with $2b$)
- test_hash_password_minimum_length: Verify enforces 8+ character minimum
- test_hash_password_no_plaintext_storage: Verify hash doesn't contain plaintext
- test_hash_password_cost_factor: Verify appropriate bcrypt cost factor (12+)
- test_hash_password_type_validation: Verify raises TypeError for non-string input

#### Edge Cases:
- test_hash_password_with_unicode: Verify handles unicode characters
- test_hash_password_maximum_length: Verify handles very long passwords
- test_hash_password_special_characters: Verify handles all special characters

#### Error Conditions:
- test_hash_password_empty_string: Verify raises ValueError for empty password
- test_hash_password_whitespace_only: Verify rejects whitespace-only password

### Function: verify_password(password: str, hashed: str) -> bool

#### Functional Tests:
- test_verify_password_correct_match: Verify returns True for correct password
- test_verify_password_incorrect_match: Verify returns False for wrong password
- test_verify_password_timing_safe: Verify constant-time comparison

#### Security Tests:
- test_verify_password_type_validation: Verify handles invalid input types safely
- test_verify_password_empty_inputs: Verify safely handles empty strings
- test_verify_password_invalid_hash_format: Verify handles corrupted hashes safely

#### Edge Cases:
- test_verify_password_unicode_characters: Verify handles unicode in password
- test_verify_password_very_long_password: Verify handles long passwords

#### Error Conditions:
- test_verify_password_none_inputs: Verify handles None values safely
- test_verify_password_malformed_hash: Verify doesn't crash on bad hash
```

## ✅ Review Checklist

Before presenting test plan to user, verify:

- [ ] All functional requirements have corresponding tests
- [ ] All security-sensitive operations have security tests
- [ ] Common edge cases are covered
- [ ] Error conditions are tested
- [ ] Test names follow convention: `test_{function}_{aspect}`
- [ ] Test descriptions are clear and specific
- [ ] Security tests reference CodeGuard files where applicable
- [ ] No duplicate or redundant tests
- [ ] Tests are achievable with pytest
- [ ] Tests align with acceptance criteria from specification

## 🤝 User Approval Process

### Present Test Plan

1. Format test plan clearly with markdown
2. Group by function/class
3. Separate by test category (functional, security, edge cases, errors)
4. Include test counts: "Total: 42 tests (15 functional, 18 security, 6 edge cases, 3 errors)"

### Request Approval

```
📋 Test Plan Ready for Review

I've created a comprehensive test plan for {module_name} with {total_count} tests:
- {functional_count} functional tests
- {security_count} security tests
- {edge_case_count} edge case tests
- {error_count} error condition tests

Please review the test plan below and let me know if you'd like to:
- ✅ Approve and proceed with implementation
- ➕ Add additional tests
- ➖ Remove unnecessary tests
- 🔄 Modify test scope or descriptions

[Test plan details follow...]
```

### Handle Feedback

User may request:

1. **Add tests**: Add to appropriate category and re-present
2. **Remove tests**: Explain impact if removing security tests, then update
3. **Modify tests**: Update descriptions/scope and re-present
4. **Clarify tests**: Provide more detail about what test verifies

### Approval Confirmation

User approves with:
- "Approved"
- "Looks good, proceed"
- "LGTM" (Looks Good To Me)
- "Go ahead"

**Only after explicit approval**, proceed to TDD implementation.

## 🚫 Common Mistakes to Avoid

1. **Starting implementation without approval**: NEVER write code before test plan is approved
2. **Skipping security tests**: Security tests are mandatory for all public functions
3. **Vague test descriptions**: Each test must clearly state what it verifies
4. **Missing edge cases**: Always consider empty, null, boundary, and extreme values
5. **Ignoring user feedback**: User knows domain better - incorporate all feedback
6. **Over-testing**: Don't test framework behavior (e.g., testing that Python's `int` works)
7. **Under-testing**: Every code path should have a corresponding test

## 💡 Tips for Effective Test Planning

1. **Start with acceptance criteria**: Every criterion should map to tests
2. **Think like an attacker**: What inputs could break security?
3. **Consider real-world usage**: What will users actually do?
4. **Reference threat model**: Use threat model to identify security tests
5. **Use CodeGuard files**: Reference relevant CodeGuard files for security test ideas
6. **Ask "what if?"**: What if input is empty? null? huge? negative? special characters?
7. **Balance coverage vs. value**: Focus on meaningful tests, not artificial 100% coverage

## 🔗 Related Documentation

- [TDD Workflow](tdd-workflow.instructions.md)
- [Generate Code from Spec Prompt](../prompts/generate-code-from-spec.prompt.md)
- [Workflow Spec to Code](../prompts/workflow-spec-to-code.prompt.md)
- [Quality Checklists](quality-checklists.md)
- CodeGuard security instruction files (for security test guidance)

---

**Version**: 1.0
**Created**: 2025-11-09