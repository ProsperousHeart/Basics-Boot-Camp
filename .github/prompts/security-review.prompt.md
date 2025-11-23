# Prompt: Security Review

**Last Updated**: 2025-11-10

**Purpose**: Conduct comprehensive security review of code implementation
**Input**: Module/package path to review
**Output**: Security review report with findings and recommendations
**References**:
- `.github/instructions/security-review.instructions.md`
- `.github/instructions/codeguard-*.instructions.md`

## Prompt

```
You are conducting a security review for: {module_path}

Follow the security review process from `.github/instructions/security-review.instructions.md`:

## Step 1: Identify Security Context

1. Read the specification at `docs/specifications/spec_{name}.md` (if exists)
2. Read the threat model at `docs/diagrams/threat-model_{name}.md` (if exists)
3. Identify security-sensitive operations:
   - Authentication/authorization
   - Data storage/retrieval
   - Input validation
   - Cryptography
   - API endpoints
   - File operations
   - Network communication

## Step 2: Apply CodeGuard Rules

Based on security context, review against relevant CodeGuard files:

- **Cryptography**: `.github/instructions/codeguard-0-additional-cryptography.instructions.md`, `codeguard-1-crypto-algorithms.instructions.md`
- **Authentication**: `.github/instructions/codeguard-0-authentication-mfa.instructions.md`
- **Authorization**: `.github/instructions/codeguard-0-authorization-access-control.instructions.md`
- **Input Validation**: `.github/instructions/codeguard-0-input-validation-injection.instructions.md`
- **API/Web**: `.github/instructions/codeguard-0-api-web-services.instructions.md`
- **Data Storage**: `.github/instructions/codeguard-0-data-storage.instructions.md`
- **File Handling**: `.github/instructions/codeguard-0-file-handling-and-uploads.instructions.md`
- **Supply Chain**: `.github/instructions/codeguard-0-supply-chain-security.instructions.md`

## Step 3: Check Common Vulnerabilities

Verify protection against OWASP Top 10:

1. **Broken Access Control**:
   - Authorization checks present
   - Privilege escalation prevented
   - Default deny access control

2. **Cryptographic Failures**:
   - No hardcoded secrets
   - Secure random number generation
   - Proper key management
   - Certificate validation

3. **Injection**:
   - SQL parameterized queries
   - Command injection prevention
   - XSS prevention (if web)
   - LDAP injection prevention

4. **Insecure Design**:
   - Threat model followed
   - Security requirements implemented
   - Defense in depth

5. **Security Misconfiguration**:
   - No default credentials
   - Secure defaults
   - Error messages don't leak info

6. **Vulnerable Components**:
   - Dependencies up to date
   - No known CVEs in requirements.txt
   - Supply chain verification

7. **Authentication Failures**:
   - MFA support (if applicable)
   - Secure session management
   - Password policies (if applicable)

8. **Data Integrity Failures**:
   - Input validation
   - Deserialization safety
   - CI/CD security

9. **Logging Failures**:
   - Security events logged
   - No PII in logs
   - Log injection prevention

10. **SSRF** (if applicable):
    - URL validation
    - Network isolation
    - Allowlist approach

## Step 4: Review Test Coverage

Verify security test cases exist for:

- Authentication edge cases
- Authorization bypass attempts
- Input validation boundary tests
- Cryptographic operations
- Error handling (no info leaks)

## Step 5: Generate Security Review Report

Create a report with these sections:

### Security Review Summary
- Module: {module_path}
- Timestamp: {current_timestamp}
- Reviewer: Claude Code
- Overall Status: ✅ PASS or ❌ FAIL or ⚠️ NEEDS REVIEW

### Security Context
- Specification reviewed: Yes/No
- Threat model reviewed: Yes/No
- Security-sensitive operations: [list]

### CodeGuard Compliance
For each applicable CodeGuard file:
- **File**: {codeguard file name}
- **Status**: ✅ COMPLIANT or ❌ NON-COMPLIANT or ⚠️ PARTIAL
- **Findings**: [specific issues or confirmations]

### OWASP Top 10 Review
For each relevant category:
- **Category**: {name}
- **Status**: ✅ PROTECTED or ❌ VULNERABLE or ⚠️ NEEDS REVIEW
- **Details**: [specific findings]

### Security Test Coverage
- ✅ ADEQUATE or ❌ INSUFFICIENT
- Tests identified: [list]
- Missing tests: [list]

### Findings

#### 🔴 Critical Issues (must fix before deployment)
- **Issue**: {description}
  - Location: {file}:{line}
  - Risk: {impact}
  - Recommendation: {how to fix}

#### 🟡 Warnings (should address)
- **Issue**: {description}
  - Location: {file}:{line}
  - Risk: {impact}
  - Recommendation: {how to fix}

#### 🔵 Recommendations (best practices)
- **Issue**: {description}
  - Location: {file}:{line}
  - Benefit: {why it helps}
  - Recommendation: {how to improve}

### Overall Assessment

**VERDICT**: ✅ SECURE / ⚠️ NEEDS FIXES / ❌ SECURITY ISSUES

**Summary**: {brief assessment}

**Next Steps**:
- If SECURE: Ready for deployment
- If NEEDS FIXES: Address warnings before deployment
- If SECURITY ISSUES: Must fix critical issues immediately
```

## Important Guidelines

- **Be thorough**: Don't skip checks because code looks simple
- **Be specific**: Cite exact line numbers and code snippets
- **Be practical**: Prioritize by risk (critical > warning > recommendation)
- **Be helpful**: Provide concrete fixes, not just problems
- **Document compliance**: Note which CodeGuard rules were followed

## Example Usage

### With Claude Code

```
Execute the security-review prompt for src/auth/login.py
```

### With GitHub Copilot

```
@workspace Conduct a security review of @src/auth/login.py following @.github/prompts/security-review.prompt.md
```

### As part of workflow

```
After code implementation and testing, run security review before final approval.
```

## Expected Output

A comprehensive security review report showing:
- Overall security status
- CodeGuard compliance assessment
- OWASP Top 10 review results
- Specific findings with severity levels
- Actionable recommendations
- Next steps based on findings

---

**Related Documentation**:
- [Security Review Instructions](../.github/instructions/security-review.instructions.md)
- [CodeGuard Guidelines](../.github/instructions/) (files prefixed with `codeguard-`)
- [Quality Checklists](../.github/instructions/quality-checklists.md)
- [Threat Modeling](../.github/instructions/threat-modeling.instructions.md)