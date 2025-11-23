# Quality Review Checklists by Stage

**Last Updated**: 2025-11-09

This document provides Definition of Done (DoD) checklists for each stage of the development workflow.

## 🎯 Purpose

- Ensure completeness at each stage
- Provide clear quality gates
- Enable consistent human reviews
- Guide AI assistants in validation

---

## 📋 Requirements Stage Quality Checklist

### Completeness

- ✅ Problem statement clearly defined
- ✅ Target users/stakeholders identified
- ✅ Success criteria are measurable
- ✅ Acceptance criteria are specific and testable
- ✅ Dependencies identified (internal and external)
- ✅ Constraints documented (technical, time, budget)
- ✅ Security considerations noted

### Clarity

- ✅ Language is unambiguous
- ✅ Technical jargon defined or avoided
- ✅ Examples provided where helpful
- ✅ Diagrams included for complex concepts
- ✅ No conflicting requirements

### Traceability

- ✅ Unique requirement ID assigned (REQ-XXX)
- ✅ Cross-referenced with related requirements
- ✅ Added to `docs/SPEC-CROSS-REFERENCE.md`
- ✅ Linked in `docs/INDEX.md`

### Template Compliance

- ✅ Uses `docs/templates/requirements-template.md`
- ✅ All template sections completed
- ✅ Saved to `docs/requirements/req-{name}.md`

### Review

- ✅ Reviewed by stakeholder(s)
- ✅ Technical feasibility confirmed
- ✅ Approved for specification stage

**Definition of Done**: All boxes checked, stakeholder approval obtained

---

## 📐 Specification Stage Quality Checklist

### Technical Completeness

- ✅ Architecture approach defined
- ✅ Technology stack specified
- ✅ Data models/schemas documented
- ✅ API contracts defined (if applicable)
- ✅ Integration points identified
- ✅ Performance requirements specified
- ✅ Scalability considerations addressed

### TDD Planning

- ✅ Test strategy outlined
- ✅ Key test scenarios identified
- ✅ Test data requirements specified
- ✅ Edge cases documented
- ✅ TDD approach documented in specification

### Security

- ✅ Threat model created/referenced
- ✅ Relevant CodeGuard files identified and referenced:
  - Authentication: `codeguard-0-authentication-mfa.instructions.md`
  - Input validation: `codeguard-0-input-validation-injection.instructions.md`
  - Cryptography: `codeguard-0-additional-cryptography.instructions.md`
  - API: `codeguard-0-api-web-services.instructions.md`
  - Data storage: `codeguard-0-data-storage.instructions.md`
  - (Add others as relevant)
- ✅ Security controls mapped to threats
- ✅ Authentication/authorization strategy defined
- ✅ Data protection approach specified

### Architecture

- ✅ Architecture diagram created
- ✅ Component responsibilities clear
- ✅ Data flow documented
- ✅ Trust boundaries marked
- ✅ Diagram saved to `docs/diagrams/architecture-{name}.md`

### Threat Modeling

- ✅ Threat model created using STRIDE
- ✅ All threat categories addressed:
  - Spoofing
  - Tampering
  - Repudiation
  - Information Disclosure
  - Denial of Service
  - Elevation of Privilege
- ✅ Mitigations defined for each threat
- ✅ Saved to `docs/diagrams/threat-model_{name}.md`

### Implementation Guidance

- ✅ Implementation steps outlined
- ✅ Module/file structure suggested
- ✅ Dependencies listed (packages to install)
- ✅ Configuration requirements specified
- ✅ Environment variables documented

### Traceability

- ✅ References originating requirement(s)
- ✅ Cross-reference table updated
- ✅ Index updated
- ✅ Links to diagrams included

### Template Compliance

- ✅ Uses `docs/templates/spec-template.md`
- ✅ All template sections completed
- ✅ Saved to `docs/specifications/spec_{name}.md`

### Review

- ✅ Technical review completed
- ✅ Security review completed
- ✅ CodeGuard compliance verified
- ✅ Approved for implementation

**Definition of Done**: All boxes checked, technical and security approval obtained

---

## 💻 Code Generation (TDD) Stage Quality Checklist

### TDD Compliance

#### RED Phase

- ✅ Test written BEFORE implementation code
- ✅ Test clearly defines expected behavior
- ✅ Test fails for the right reason
- ✅ Test follows naming convention: `test_{behavior}_description`

#### GREEN Phase

- ✅ Minimal code written to pass test
- ✅ Test now passes
- ✅ No over-engineering

#### REFACTOR Phase

- ✅ Code improved while tests stay green
- ✅ Duplication removed
- ✅ Readability enhanced
- ✅ Naming improved

### Test Quality

- ✅ Unit tests cover all functions/methods
- ✅ Integration tests cover component interactions
- ✅ Edge cases tested
- ✅ Error conditions tested
- ✅ Security scenarios tested (for sensitive code)
- ✅ Test coverage ≥ 90%
- ✅ All tests pass
- ✅ No skipped tests without justification

### Test Structure

- ✅ Test directory mirrors `src/` structure
- ✅ Test files named `test_{module_name}.py`
- ✅ Tests use AAA pattern (Arrange, Act, Assert)
- ✅ Tests are independent (no shared state)
- ✅ Tests are repeatable

### Code Quality

- ✅ Ruff checks pass (linting)
- ✅ Ruff format applied
- ✅ No TODO comments without tracking issue
- ✅ No commented-out code
- ✅ No debug print statements

### Documentation

- ✅ Module has ABOUTME comment (2 lines)
- ✅ Module docstring present
- ✅ All public functions have docstrings
- ✅ All classes have docstrings
- ✅ Docstrings follow `docs/rules/docstring-standards.md`
- ✅ Type hints in function signatures
- ✅ Examples in docstrings for complex functions

### Security

- ✅ CodeGuard rules applied and documented
- ✅ No hardcoded credentials or secrets
- ✅ Secrets loaded from environment variables
- ✅ Input validation implemented
- ✅ Error messages don't leak sensitive data
- ✅ Logging doesn't capture PII or credentials
- ✅ Security test cases pass

### Traceability

- ✅ Cross-reference table updated with source and test files
- ✅ Execution log created in `docs/output-logs/` or `.github/prompts/output-logs/`
- ✅ Error KB updated if self-fixes occurred

### Review

- ✅ Automated tests pass
- ✅ Security review pass (follows `security-review.instructions.md`)
- ✅ Code review completed
- ✅ Approved for quality stage

**Definition of Done**: All boxes checked, all tests green, security review passed

---

## ✅ Quality Stage Quality Checklist

### Test Validation

- ✅ All unit tests pass
- ✅ All integration tests pass (if applicable)
- ✅ Test coverage meets threshold (90%+)
- ✅ No flaky tests
- ✅ Performance tests pass (if applicable)

### Static Analysis

- ✅ Ruff linting passes
- ✅ Ruff formatting passes
- ✅ Type checking passes (if using mypy/pyright)
- ✅ No security warnings from bandit (if used)
- ✅ No critical issues from safety scan (if used)

### Security Audit

- ✅ Security review checklist completed
- ✅ CodeGuard compliance verified
- ✅ Threat model mitigations implemented
- ✅ Penetration testing completed (if applicable)
- ✅ Dependency vulnerabilities checked

### Documentation Validation

- ✅ All docs updated
- ✅ Cross-reference table accurate
- ✅ Index up to date
- ✅ READMEs current
- ✅ API documentation generated (if applicable)

### Integration

- ✅ Integration with existing codebase verified
- ✅ No breaking changes (or documented if necessary)
- ✅ Backward compatibility maintained (or documented)
- ✅ Database migrations tested (if applicable)

### Post-Test Review

- ✅ Follows `post-test-review.instructions.md`
- ✅ All checklist items addressed

### Final Approval

- ✅ Technical lead approval
- ✅ Security approval (for security-sensitive code)
- ✅ Product owner approval (if applicable)
- ✅ Ready for deployment/merge

**Definition of Done**: All boxes checked, all approvals obtained

---

## 🔄 Using These Checklists

### For Human Reviewers

1. Copy relevant checklist to review notes
2. Check each box as you verify
3. Document any issues found
4. Request changes if DoD not met
5. Approve when all boxes checked

### For AI Assistants

When conducting reviews, reference this file:

```
Conduct {stage} quality review following quality-checklists.md
```

AI should:

- Verify each checklist item
- Report which items pass/fail
- Suggest fixes for failures
- Update execution log with results

### Example Output

```markdown
## Requirements Stage Quality Review

### Completeness

- ✅ Problem statement clearly defined
- ✅ Target users/stakeholders identified
- ❌ Success criteria not measurable (ISSUE: criteria too vague)
- ✅ Acceptance criteria specific and testable
  ...

**Result**: ❌ Failed - 1 issue found
**Action Needed**: Clarify success criteria with measurable metrics
```

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [Security Review](security-review.instructions.md)
- [Post-Test Review](post-test-review.instructions.md)
- [TDD Workflow](tdd-workflow.instructions.md)
- [Output Format](../../docs/rules/output-format.md)

---

**TODO**: As the template evolves, add stage-specific quality metrics and thresholds
