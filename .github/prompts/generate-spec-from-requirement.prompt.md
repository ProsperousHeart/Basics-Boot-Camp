# Prompt: Generate Specification from Requirement

**Purpose**: Convert a requirement document into a technical specification
**Input**: Requirement document path
**Output**: Specification document in `docs/specifications/`
**References**:

- `docs/templates/spec-template.md`
- `.github/instructions/master-workflow.md`
- Relevant CodeGuard instruction files

## Prompt

```
Generate a technical specification from the requirement document at {requirement_path}.

Follow these steps carefully:

### Step 1: Validate Prerequisites

- Check if {requirement_path} exists
  - If the file doesn't exist, inform the user and suggest available requirements files in docs/requirements/ or offer to make an initial requirement.
  - Exit with a helpful error message
- Verify docs/templates/spec-template.md exists
- Verify docs/specifications/ directory exists (create if missing)

### Step 2: Read Requirements and Template

- **Read the full content of the requirement document** at {requirement_path}
- **Read the specification template** docs/templates/spec-template.md to understand the expected structure
- Identify the component/feature name from the requirement

### Step 3: Generate the Specification

**Create a detailed specification** following the requirements & template structure with these sections:

- **Context**: Purpose, role in application, users, usage, system integration
- **Requirements**: Functional and nonfunctional requirements, interface requirements, data requirements, integration requirements, UI requirements
- **Constraints**: Technical stack, performance requirements, design constraints, security constraints, file structure/naming convnentions, deployment constraints
- **Technical Approach**: Architecture overview, design patterns, data flow diagrams, component interactions
- **Acceptance Criteria**: Testable success criteria as checkboxes, edge cases, UX validation, integration points, functionality, quality, integration, security, documentation, deployment
- **Implementation Plan**: Step-by-step plan, milestones, timelines, resource allocation

Important considerations:
- Include technical approach and architecture decisions
- Identify and reference relevant CodeGuard security instruction files from .github/instructions/
- Create threat model reference if security-sensitive
- Include implementation plan with clear steps
- Ensure all sections from the template are addressed

### Step 4: Save and Update Documentation

- Save the specification to docs/specifications/spec_{name}.md
- Update docs/SPEC-CROSS-REFERENCE.md with the new specification
- Update docs/INDEX.md with links to the new spec
- Log the execution details to docs/output-logs/{timestamp}-spec-generation.md
- update any relevant diagrams in docs/diagrams/README.md if applicable
- Ensure proper formatting and markdown syntax throughout
- Validate links and references
- Ensure compliance with documentation standards
- Review for clarity, completeness, and accuracy
- Check for consistency with existing specifications
- ensure instructions for Claude and copilot are updated to include the new spec generation process as needed
- Prepare for human review and approval

### Step 5: Confirm Completion

Report to the user:
- ✅ Spec file created successfully at docs/specifications/spec_{name}.md
- 📋 Brief summary of what was specified
- 🔒 CodeGuard files referenced and why they're relevant
- 🔗 Links to updated documentation (cross-reference, index)
- ⏭️ Next step: Create threat model and architecture diagram (**Security Considerations**: Threat model, data protection, authentication/authorization, compliance, relevant CodeGuard files)
```

## Example Usage

### With Claude Code

```
Use the generate-spec-from-requirement prompt for docs/requirements/req-auth.md
```

### With GitHub Copilot

```
@workspace Generate a technical specification from @docs/requirements/req-auth.md using the template at @docs/templates/spec-template.md. Reference relevant CodeGuard security files and update the cross-reference table.
```

## Expected Output

- New file: `docs/specifications/spec_{name}.md`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Updated: `docs/INDEX.md`
- Log file: `docs/output-logs/{timestamp}-spec-generation.md`

**TODO**: Add complete example of generated specification
