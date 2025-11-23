# Output Logs

This folder contains execution logs from AI-assisted workflow operations.

## 📋 Purpose

Execution logs provide:
- Traceability of automated operations
- Record of which CodeGuard rules were applied
- Issues encountered and resolutions
- Audit trail for compliance

## 📁 Log Types

- `{timestamp}-spec-generation.md` - Specification generation logs
- `{timestamp}-code-generation.md` - Code generation logs (TDD cycles)
- `{timestamp}-threat-modeling.md` - Threat model creation logs
- `{timestamp}-architecture-diagram.md` - Architecture diagram creation logs
- `{timestamp}-security-review.md` - Security review logs
- `{timestamp}-doc-update.md` - Documentation update logs

## 🔒 Privacy & Gitignore

**This folder is gitignored by default** to avoid committing potentially sensitive execution details.

To track logs in git:
1. Edit `.gitignore`
2. Comment out or remove: `.github/prompts/output-logs/*.md`
3. Commit logs as needed

## 📝 Log Format

Each log should follow `docs/rules/output-format.md` and include:

```markdown
# Execution Log: {Operation}

**Date**: YYYY-MM-DD HH:MM:SS
**Operation**: {What was done}
**Input**: {Source documents}
**Output**: {Generated files}

## Phases Completed

1. [✓] Phase 1 description
2. [✓] Phase 2 description
3. [✓] Phase 3 description

## CodeGuard Rules Applied

- codeguard-0-authentication-mfa.instructions.md - Reason
- codeguard-0-input-validation-injection.instructions.md - Reason

## Guidelines Followed

- tdd-workflow.instructions.md
- docstring-standards.md

## Issues Encountered

### Issue 1: Description
- **Error**: Error message
- **Resolution**: How it was fixed
- **Updated**: error-resolution-kb.md (if applicable)

## Test Results

[Test output if applicable]

## Summary

[Brief summary of what was accomplished]
```

## 🗑️ Cleanup

Logs can be deleted periodically as they're for reference only. Consider keeping:
- Recent logs (last 30 days)
- Logs from major milestones
- Logs documenting important decisions

---

**Note**: This README is tracked in git to ensure the folder exists in the repository structure.
