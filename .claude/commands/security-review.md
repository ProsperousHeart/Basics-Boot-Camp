Execute the security review prompt at `.github/prompts/security-review.prompt.md` for module: {{$1}}

This command conducts a comprehensive security review of code implementation.

**Usage:**

```
/security-review src/auth/login.py
/security-review src/api/
```

**What it does:**

1. **Identifies Security Context**: Reviews spec and threat model
2. **Applies CodeGuard Rules**: Checks compliance with relevant CodeGuard guidelines
3. **Checks Common Vulnerabilities**: Reviews against OWASP Top 10
4. **Reviews Test Coverage**: Verifies security test cases exist
5. **Generates Security Report**: Detailed findings and recommendations

**CodeGuard Areas Reviewed:**

- Cryptography (algorithms, key management)
- Authentication/Authorization
- Input Validation (SQL injection, XSS, command injection)
- API/Web Services security
- Data Storage security
- File Handling security
- Supply Chain security

**OWASP Top 10 Checks:**

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Data Integrity Failures
9. Logging Failures
10. SSRF

**Output:**

- Security review report with severity levels:
  - 🔴 **Critical**: Must fix before deployment
  - 🟡 **Warning**: Should address
  - 🔵 **Recommendation**: Best practices

**Report Sections:**

- Security Context
- CodeGuard Compliance
- OWASP Top 10 Review
- Security Test Coverage
- Findings (Critical/Warning/Recommendation)
- Overall Assessment
- Next Steps

**Verdict:**

- ✅ **SECURE**: Ready for deployment
- ⚠️ **NEEDS FIXES**: Address warnings before deployment
- ❌ **SECURITY ISSUES**: Must fix critical issues immediately

**Next Steps:**

- If SECURE: Proceed to deployment
- If NEEDS FIXES: Address warnings
- If SECURITY ISSUES: Fix critical issues and re-review

**Note:** This command delegates to the tool-agnostic prompt at `.github/prompts/security-review.prompt.md`