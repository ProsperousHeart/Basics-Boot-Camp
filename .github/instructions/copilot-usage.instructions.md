# GitHub Copilot Usage Instructions

**Last Updated**: 2025-11-09

This document explains how to use GitHub Copilot with this Python template repository.

## 🎯 Overview

GitHub Copilot can assist with all stages of the development workflow defined in this template. When properly configured, it references instructions, applies CodeGuard security rules, and maintains documentation standards.

## 📋 Setup

### 1. Copilot Configuration

Create or update `.github/copilot-instructions.md` to reference this template's structure:

```markdown
# GitHub Copilot Instructions

This project uses a specification-driven development workflow. Please reference:

- Documentation structure in `docs/`
- Development instructions in `.github/instructions/`
- CodeGuard security guidelines in `.github/instructions/codeguard-*.instructions.md`
- Project standards in `docs/rules/`

## Key Files

- Master workflow: `.github/instructions/master-workflow.md`
- TDD workflow: `.github/instructions/tdd-workflow.instructions.md`
- Docstring standards: `docs/rules/docstring-standards.md`
- Cross-reference table: `docs/SPEC-CROSS-REFERENCE.md`
```

**TODO**: Add complete Copilot configuration example

### 2. Enable Copilot Instructions

Ensure Copilot instructions are enabled in your IDE settings.

**TODO**: Add IDE-specific setup steps (VSCode, JetBrains, etc.)

## 🔄 Using Copilot in the Workflow

### Stage 1: Environment Setup

**Use `@workspace` command**:
```
@workspace Set up UV environment
```

Reference: `@.github/instructions/uv-environment-setup.instructions.md`

**TODO**: Add example interactions

### Stage 2: Requirements

**Use `@workspace` command**:
```
@workspace Create a requirement for user authentication using @docs/templates/requirements-template.md
```

**TODO**: Add example interactions

### Stage 3: Threat Models & Diagrams

**Use `@workspace` command**:
```
@workspace Generate threat model for @docs/requirements/req-auth.md following @.github/instructions/threat-modeling.instructions.md
```

**TODO**: Add example interactions

### Stage 4: Specifications

**Use `@workspace` command**:
```
@workspace Generate specification from @docs/requirements/req-auth.md using @docs/templates/spec-template.md
```

**TODO**: Add example interactions

### Stage 5: Code Generation (TDD)

**Use `@workspace` command**:
```
@workspace Implement @docs/specifications/spec_auth.md using TDD (@.github/instructions/tdd-workflow.instructions.md)
```

Copilot will:
- Write tests first (RED)
- Suggest implementation (GREEN)
- Assist with refactoring (REFACTOR)

**Important**: Manually verify CodeGuard rules are being followed

**TODO**: Add example interactions

### Stage 6: Quality Review

**Use inline chat**:
```
Review this code for security issues, reference @.github/instructions/security-review.instructions.md
```

**TODO**: Add example interactions

## 🔒 CodeGuard Integration

Unlike Claude Code, Copilot doesn't automatically apply CodeGuard rules. You must explicitly reference them:

```
@workspace Review authentication code against @.github/instructions/codeguard-0-authentication-mfa.instructions.md
```

**Best practice**: Create code review checklist that references relevant CodeGuard files.

**TODO**: Add CodeGuard checklist template

## 📝 Using @-mentions Effectively

### Reference Files
```
@docs/requirements/req-001.md
@.github/instructions/master-workflow.md
@docs/rules/docstring-standards.md
```

### Reference Folders
```
@docs/diagrams
@.github/instructions
```

### Use @workspace for Context-Aware Questions
```
@workspace What's the structure of the documentation system?
@workspace How do I add a new requirement?
```

**TODO**: Add comprehensive @-mention examples

## ✅ Best Practices

- [ ] Always use `@workspace` for workflow questions
- [ ] Reference specific instruction files with `@` mentions
- [ ] Explicitly ask for CodeGuard compliance
- [ ] Manually update cross-reference table (Copilot can help but won't do automatically)
- [ ] Review generated code against standards
- [ ] Verify TDD approach is followed

**TODO**: Expand best practices

## 🐛 Troubleshooting

### Copilot doesn't see instructions

**TODO**: Add troubleshooting steps

### Suggestions don't follow standards

**TODO**: Add troubleshooting steps

### CodeGuard rules not applied

**Solution**: Copilot requires explicit prompting. Always reference CodeGuard files directly.

**TODO**: Add more troubleshooting scenarios

## 🔄 Copilot vs Claude Code

| Feature | GitHub Copilot | Claude Code |
|---------|----------------|-------------|
| Auto-apply CodeGuard | ❌ Manual | ✅ Automatic |
| TDD Workflow | 🟡 Assists | ✅ Full automation |
| Doc Updates | 🟡 Suggests | ✅ Automatic |
| Threat Modeling | 🟡 Assists | ✅ Full automation |
| Context Awareness | @-mentions | Full project |

**TODO**: Expand comparison table

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [Claude Code Usage](claude-usage.instructions.md)
- [Prompts](../.github/prompts/)

---

**TODO**: This is a placeholder. Expand with:
- Detailed setup instructions for different IDEs
- Complete workflow examples
- Copilot Chat best practices
- Advanced features (Copilot for PRs, etc.)
- Integration with CI/CD
