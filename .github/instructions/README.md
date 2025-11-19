# Instructions & Guidelines

This folder contains universal how-to guides, workflows, and instructions for developing with this Python template repository. These instructions are tool-agnostic and work with both human developers and AI assistants (Claude Code, GitHub Copilot).

## 📖 Table of Contents

### Core Workflows
- **[Master Workflow](master-workflow.md)** - Complete end-to-end development process
- **[TDD Workflow](tdd-workflow.instructions.md)** - Test-Driven Development (RED-GREEN-REFACTOR)
- **[UV Environment Setup](uv-environment-setup.instructions.md)** - Virtual environment management

### Specialized Processes
- **[Threat Modeling](threat-modeling.instructions.md)** - Creating security threat models
- **[Architecture Diagrams](architecture-diagrams.instructions.md)** - Generating architecture diagrams with Mermaid
- **[Automation Setup](automation-setup.instructions.md)** - GitHub Actions, pre-commit hooks, and scripts

### Quality & Security
- **[Quality Checklists](quality-checklists.md)** - Definition of Done for each workflow stage
- **[Security Review](security-review.instructions.md)** - Security review process
- **[Post-Test Review](post-test-review.instructions.md)** - Quality review after testing
- **[Test Case Generation](testcase.instructions.md)** - Writing comprehensive test cases

### AI Assistant Usage
- **[Claude Code Usage](claude-usage.instructions.md)** - Using Claude Code with this template
- **[GitHub Copilot Usage](copilot-usage.instructions.md)** - Using GitHub Copilot with this template

### CodeGuard Security Guidelines
This folder also contains CodeGuard security instruction files (prefix: `codeguard-*`). These provide secure-by-default patterns for:
- Cryptography
- Authentication & Authorization
- Input Validation & Injection Prevention
- API & Web Services
- Cloud Security
- Supply Chain Security
- And more...

See [CodeGuard Documentation](https://project-codeguard.org/) for details.

## 🚀 Quick Start

### For Human Developers

1. **Setup**: Follow [UV Environment Setup](uv-environment-setup.instructions.md)
2. **Workflow**: Read [Master Workflow](master-workflow.md) for the complete development process
3. **Security**: Review relevant CodeGuard files before implementing security-sensitive features

### For AI Assistants

- **Claude Code**: Follow [claude-usage.instructions.md](claude-usage.instructions.md)
- **GitHub Copilot**: Follow [copilot-usage.instructions.md](copilot-usage.instructions.md)

## 📋 How Instructions Are Used

### In Development Workflow

1. **Requirements Stage**:
   - Create requirements using templates
   - Generate threat models ([threat-modeling.instructions.md](threat-modeling.instructions.md))
   - Generate architecture diagrams ([architecture-diagrams.instructions.md](architecture-diagrams.instructions.md))

2. **Specification Stage**:
   - Generate specs from requirements
   - Apply relevant CodeGuard security patterns

3. **Implementation Stage**:
   - Follow TDD workflow ([tdd-workflow.instructions.md](tdd-workflow.instructions.md))
   - Use UV environment management ([uv-environment-setup.instructions.md](uv-environment-setup.instructions.md))
   - Apply CodeGuard security guidelines automatically

4. **Quality Stage**:
   - Validate against quality checklists ([quality-checklists.md](quality-checklists.md))
   - Run post-test review ([post-test-review.instructions.md](post-test-review.instructions.md))
   - Conduct security review ([security-review.instructions.md](security-review.instructions.md))

## 🔧 Automation

Instructions can be automated using:
- **GitHub Actions** - CI/CD workflows
- **Pre-commit Hooks** - Local validation before commits
- **Manual Scripts** - On-demand execution

See [automation-setup.instructions.md](automation-setup.instructions.md) for implementation details.

## 📝 Adding New Instructions

When adding new instruction files, **follow the Meta-Documentation Checklist** at `../.github/META-CHECKLIST.md`.

Quick checklist:

1. Use descriptive filenames ending in `.instructions.md`
2. Include clear step-by-step guidance
3. Add examples where helpful
4. Update this README with a link and description
5. Reference from relevant prompts in `../.github/prompts/`
6. Update CHANGELOG.md

**See `../META-CHECKLIST.md` for complete synchronization requirements.**

## 🔗 Related Documentation

- **[Prompts](../.github/prompts/)** - AI prompt templates that reference these instructions
- **[Documentation Hub](../../docs/)** - Project-specific documentation
- **[Rules](../../docs/rules/)** - Project standards and conventions

## 📦 Template Repository Note

This is a **template repository**. When you create a new project from this template:
- All instruction files remain as universal guidelines
- CodeGuard files provide security best practices
- You customize `docs/` for your specific project
- You can add project-specific instructions as needed

---

**Last Updated**: 2025-11-09
