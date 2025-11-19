# AI Prompts

This folder contains reusable prompt templates for common AI-assisted operations in the development workflow.

## 📋 Available Prompts

### Workflow Orchestration Prompts
- **[workflow-requirements-to-spec.prompt.md](workflow-requirements-to-spec.prompt.md)** - Complete workflow: Requirements → Specification (includes spec generation, threat model, architecture diagram, and quality review)
- **[workflow-spec-to-code.prompt.md](workflow-spec-to-code.prompt.md)** - Complete workflow: Specification → Code (includes TDD implementation, security review, and quality validation)

### Individual Operation Prompts
- **[generate-spec-from-requirement.prompt.md](generate-spec-from-requirement.prompt.md)** - Convert requirement to technical specification
- **[generate-code-from-spec.prompt.md](generate-code-from-spec.prompt.md)** - Generate code from specification using TDD
- **[create-threat-model.prompt.md](create-threat-model.prompt.md)** - Create security threat model using STRIDE
- **[create-architecture-diagram.prompt.md](create-architecture-diagram.prompt.md)** - Generate architecture diagram (text/ASCII/Mermaid)
- **[verify-implementation.prompt.md](verify-implementation.prompt.md)** - Comprehensive verification of code implementation
- **[security-review.prompt.md](security-review.prompt.md)** - Conduct security review with CodeGuard compliance
- **[update-documentation.prompt.md](update-documentation.prompt.md)** - Update documentation indexes and cross-references

## 🎯 How to Use Prompts

### With Claude Code

Reference prompts in your requests:
```
Use the generate-spec-from-requirement prompt for REQ-001
```

### With GitHub Copilot

Copy prompt content and paste into Copilot chat with context:
```
@workspace [paste prompt here] for @docs/requirements/req-001.md
```

## 📝 Prompt Structure

Each prompt file follows this structure:

```markdown
# Prompt: {Name}

**Purpose**: {What this prompt does}
**Input**: {What information is needed}
**Output**: {What will be generated}
**References**: {Which instruction files are relevant}

## Prompt

{Actual prompt text that can be copied and used}

## Example Usage

{Example of using this prompt}
```

## 📂 Output Logs

Execution logs from using these prompts are saved to `output-logs/` (gitignored by default).

## 🔗 Related Documentation

- [Instructions](../instructions/) - How-to guides referenced by prompts
- [Master Workflow](../instructions/master-workflow.md) - Complete workflow overview
- [Claude Usage](../instructions/claude-usage.instructions.md) - Using prompts with Claude
- [Copilot Usage](../instructions/copilot-usage.instructions.md) - Using prompts with Copilot
- [Claude Commands](../../.claude/commands/) - Claude Code slash commands that delegate to these prompts
- [Meta-Checklist](../META-CHECKLIST.md) - Checklist for keeping documentation synchronized
