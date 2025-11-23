# Security Review Instructions

**Last Updated**: 2025-11-09

This document provides guidance for conducting security reviews during the quality stage of development.

## 🎯 Overview

Security reviews ensure that code follows secure-by-default practices and complies with CodeGuard guidelines. This review happens after code generation and before human approval.

## 📋 Review Process

### Stage 1: Automated Security Checks

**Tools:**

- Bandit (Python security linter)
- Safety (dependency vulnerability scanner)
- Ruff (with security rules enabled)

**TODO**: Add tool setup and configuration

### Stage 2: CodeGuard Compliance Check

Verify that relevant CodeGuard instruction files were followed:

**Checklist by Domain:**

#### Authentication (`codeguard-0-authentication-mfa.instructions.md`)

- [ ] MFA supported where appropriate
- [ ] Passwords never logged or stored in plaintext
- [ ] Session management follows best practices
- [ ] OAuth/OIDC implemented correctly

**TODO**: Add complete authentication checklist

#### Input Validation (`codeguard-0-input-validation-injection.instructions.md`)

- [ ] All user inputs validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Command injection prevention

**TODO**: Add complete input validation checklist

#### Cryptography (`codeguard-0-additional-cryptography.instructions.md`, `codeguard-1-crypto-algorithms.instructions.md`)

- [ ] Strong algorithms used (AES-256, RSA-2048+)
- [ ] No hardcoded keys or secrets
- [ ] Proper key management
- [ ] TLS/SSL configured correctly

**TODO**: Add complete cryptography checklist

#### API Security (`codeguard-0-api-web-services.instructions.md`)

- [ ] Authentication required on endpoints
- [ ] Rate limiting implemented
- [ ] CORS configured properly
- [ ] Input validation on all endpoints

**TODO**: Add complete API security checklist

#### Data Storage (`codeguard-0-data-storage.instructions.md`)

- [ ] Sensitive data encrypted at rest
- [ ] Database credentials stored securely
- [ ] Access controls implemented
- [ ] Audit logging enabled

**TODO**: Add complete data storage checklist

#### Session Management (`codeguard-0-session-management-and-cookies.instructions.md`)

- [ ] Secure cookie flags set (HttpOnly, Secure, SameSite)
- [ ] Session timeouts configured
- [ ] Session regeneration after privilege change
- [ ] CSRF protection implemented

**TODO**: Add complete session management checklist

### Stage 3: Threat Model Verification

Compare implementation against threat model:

1. Open threat model: `docs/diagrams/threat-model-{name}.md`
2. Verify mitigations implemented
3. Check for new threats introduced
4. Update threat model if needed (create new version)

**TODO**: Add threat model verification checklist

### Stage 4: Manual Code Review

**Focus areas:**

- Authorization logic
- Secret handling
- Error messages (no sensitive data leaked)
- Logging (no PII or credentials logged)
- Third-party dependencies

**TODO**: Add manual review checklist

## 🔒 Security Review Checklist

### General Security

- [ ] No hardcoded credentials or API keys
- [ ] Secrets loaded from environment variables or secure vault
- [ ] Error messages don't expose sensitive information
- [ ] Logging doesn't capture PII or credentials
- [ ] Dependencies are up-to-date and vulnerability-free

### CodeGuard Compliance

- [ ] Relevant CodeGuard files identified for this code
- [ ] Each CodeGuard recommendation addressed or documented why not
- [ ] Execution logs show which CodeGuard rules were applied
- [ ] Security controls match threat model mitigations

### Testing

- [ ] Security test cases exist
- [ ] Edge cases and attack vectors tested
- [ ] Error handling doesn't leak sensitive data
- [ ] Authentication/authorization thoroughly tested

**TODO**: Expand checklist with specific criteria

## 📝 Security Review Report Template

```markdown
# Security Review: {Feature Name}

**Specification**: [SPEC-XXX](../specifications/spec_xxx.md)
**Date**: YYYY-MM-DD
**Reviewer**: [Name or "Automated"]

## CodeGuard Files Reviewed

- [ ] codeguard-0-authentication-mfa.instructions.md
- [ ] codeguard-0-input-validation-injection.instructions.md
- [ ] [Add others as relevant]

## Findings

### High Priority

None

### Medium Priority

None

### Low Priority

None

### Informational

None

## Threat Model Verification

- [ ] All mitigations from threat model implemented
- [ ] No new threats introduced
- [ ] Threat model updated if needed: [link to new version]

## Recommendations

[Any security improvements or follow-up items]

## Approval

- [ ] Security review passed
- [ ] Ready for human approval

**Reviewer Signature**: ******\_\_\_******
**Date**: ******\_\_\_******
```

**TODO**: Add complete report template

## 🤖 AI Assistant Integration

### For Claude Code

```
Conduct security review for SPEC-001 implementation following security-review.instructions.md
```

Claude will:

- Run automated security checks
- Verify CodeGuard compliance
- Generate security review report
- Update error KB if issues found

**TODO**: Add Claude-specific examples

### For GitHub Copilot

```
@workspace Review this code for security issues using @.github/instructions/security-review.instructions.md
```

**TODO**: Add Copilot-specific examples

## 🐛 Common Security Issues

### Issue: Hardcoded Credentials

**Example:**

```python
# ❌ Bad
API_KEY = "hardcoded-api-key-example-do-not-do-this"

# ✅ Good
import os
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

**CodeGuard Reference**: `codeguard-1-hardcoded-credentials.instructions.md`

**TODO**: Add more common issues and solutions

### Issue: SQL Injection

**TODO**: Add SQL injection examples

### Issue: XSS Vulnerability

**TODO**: Add XSS examples

### Issue: Insecure Cryptography

**TODO**: Add cryptography examples

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [Threat Modeling](threat-modeling.instructions.md)
- [Post-Test Review](post-test-review.instructions.md)
- [CodeGuard Files](.) - All codeguard-\*.instructions.md
- [Error Resolution KB](../../docs/rules/error-resolution-kb.md)

---

**TODO**: This is a placeholder. Expand with:

- Complete security checklists for all CodeGuard domains
- Automated security scanning setup
- Common vulnerability examples and fixes
- Security testing best practices
- Integration with CI/CD security scanning
