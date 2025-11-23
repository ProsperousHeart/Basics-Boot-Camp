# Prompt: Create Architecture Diagram

**Purpose**: Generate architecture diagram using Mermaid
**Input**: Requirement or specification document path
**Output**: Architecture diagram in `docs/diagrams/`
**References**:
- `.github/instructions/architecture-diagrams.instructions.md`
- Relevant CodeGuard instruction files

## Prompt

```
Create an architecture diagram for {document_path}.

Instructions:
1. Read the requirement or specification document
2. Follow guidance in .github/instructions/architecture-diagrams.instructions.md
3. Create appropriate Mermaid diagrams:
   - System architecture (component interactions)
   - Sequence diagrams (if workflow-heavy)
   - ERD diagrams (if database-intensive)
   - Component diagrams (if modular architecture)
4. Include:
   - Component descriptions
   - Technology choices
   - Security annotations (trust boundaries, encryption, auth points)
   - References to relevant CodeGuard files
5. Save to docs/diagrams/ with appropriate prefix:
   - architecture-{name}.md
   - sequence-{name}.md
   - erd-{name}.md
   - component-{name}.md
6. Optionally create separate .mmd file if requested
7. Update docs/SPEC-CROSS-REFERENCE.md
8. Log execution details to docs/output-logs/{timestamp}-architecture-diagram.md

Note: When updating existing diagrams, create a new version file rather than editing the original.
```

## Example Usage

### With Claude Code

```
Use the create-architecture-diagram prompt for docs/specifications/spec_api.md
```

### With GitHub Copilot

```
@workspace Create architecture diagram for @docs/specifications/spec_api.md using Mermaid following @.github/instructions/architecture-diagrams.instructions.md
```

## Expected Output

- Architecture diagram: `docs/diagrams/architecture_{name}.md`
- Optional: `docs/diagrams/architecture_{name}.mmd`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Log: `docs/output-logs/{timestamp}-architecture-diagram.md`

**TODO**: Add complete architecture diagram example
