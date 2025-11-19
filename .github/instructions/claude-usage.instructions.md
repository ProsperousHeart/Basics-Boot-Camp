# Claude Code Usage Instructions

**Last Updated**: 2025-11-09

This document explains how to use Claude Code with this Python template repository.

## 🎯 Overview

Claude Code can assist with all stages of the development workflow defined in this template. It automatically references instructions, applies CodeGuard security rules, and maintains documentation.

## 📋 Setup

### 1. Claude Configuration

Claude Code reads configuration from:
- `.claude/CLAUDE.md` (project-specific instructions)
- `CLAUDE.md` (project root instructions)
- `.github/instructions/` (universal guidelines)

**TODO**: Add detailed setup steps

### 2. Verify Access

Ensure Claude can access:
- All `.md` files in `docs/`
- All instruction files in `.github/instructions/`
- All prompt files in `.github/prompts/`
- Source code in `src/` and `test/`

**TODO**: Add verification checklist

## 🔄 Using Claude in the Workflow

### Stage 1: Environment Setup

**Prompt Claude**:
```
Set up the UV environment following the uv-environment-setup instructions
```

Claude will:
- Check for existing environment
- Create if needed
- Use `uv add` for packages

**TODO**: Add example interactions

### Stage 2: Requirements

**Prompt Claude**:
```
Create a new requirement for [feature description] using the requirements template
```

Claude will:
- Use `docs/templates/requirements-template.md`
- Create `docs/requirements/req-{name}.md`
- Update cross-reference table

**TODO**: Add example interactions

### Stage 3: Threat Models & Diagrams

**Prompt Claude**:
```
Generate a threat model and architecture diagram for REQ-001
```

Claude will:
- Reference `threat-modeling.instructions.md`
- Reference `architecture-diagrams.instructions.md`
- Apply STRIDE framework
- Create Mermaid diagrams
- Reference relevant CodeGuard files
- Save to `docs/diagrams/`

**TODO**: Add example interactions

### Stage 4: Specifications

**Prompt Claude**:
```
Generate a specification from REQ-001
```

Claude will:
- Use `docs/templates/spec-template.md`
- Reference requirement document
- Include security considerations
- Link CodeGuard files
- Update cross-reference table

**TODO**: Add example interactions

### Stage 5: Code Generation (TDD)

**Prompt Claude**:
```
Implement SPEC-001 using TDD
```

Claude will:
- Follow `tdd-workflow.instructions.md`
- Write tests first (RED)
- Implement code (GREEN)
- Refactor (REFACTOR)
- Apply relevant CodeGuard rules automatically
- Follow docstring standards
- Log execution details

**TODO**: Add example interactions

### Stage 6: Quality Review

**Prompt Claude**:
```
Run quality review for the implementation
```

Claude will:
- Run ruff checks
- Run pytest
- Follow `post-test-review.instructions.md`
- Follow `security-review.instructions.md`
- Update error KB if issues found

**TODO**: Add example interactions

## 🔒 CodeGuard Integration

Claude automatically references CodeGuard instruction files based on the code being generated:

- **Authentication code** → `codeguard-0-authentication-mfa.instructions.md`
- **API code** → `codeguard-0-api-web-services.instructions.md`
- **Database code** → `codeguard-0-data-storage.instructions.md`
- **Crypto code** → `codeguard-0-additional-cryptography.instructions.md`
- etc.

**Verification**: Check execution logs in `docs/output-logs/` to see which CodeGuard rules were applied.

**TODO**: Add CodeGuard verification examples

## 📝 Custom Prompts

Use pre-defined prompts from `.github/prompts/`:

```
Use the generate-spec-from-requirement prompt for REQ-001
```

**TODO**: Add custom prompt examples

## ✅ Best Practices

- [ ] Always reference instruction files explicitly when needed
- [ ] Ask Claude to log execution details
- [ ] Verify CodeGuard rules are being applied
- [ ] Check cross-reference table is updated
- [ ] Review generated documentation
- [ ] Confirm tests are written before code (TDD)

**TODO**: Expand best practices

## 🐛 Troubleshooting

### Claude doesn't reference instructions

**TODO**: Add troubleshooting steps

### CodeGuard rules not applied

**TODO**: Add troubleshooting steps

### Documentation not updated

**TODO**: Add troubleshooting steps

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [GitHub Copilot Usage](copilot-usage.instructions.md)
- [Prompts](../.github/prompts/)

---

**TODO**: This is a placeholder. Expand with:
- Detailed setup instructions
- Complete workflow examples
- Troubleshooting guide
- Advanced Claude Code features
- Integration with other tools
