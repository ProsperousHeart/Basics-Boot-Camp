# Workflow Prompt: Requirements → Specification (Complete)

**Purpose**: Orchestrate the complete workflow from requirement to approved specification
**Input**: Requirement document path
**Output**: Specification, threat model, architecture diagram, updated documentation
**References**: Multiple prompts and instructions

## 🔄 Workflow Overview

This prompt orchestrates the complete Requirements → Specification workflow including:

1. Specification generation
2. Threat model creation
3. Architecture diagram creation
4. Quality review
5. Documentation updates

## 📋 Master Orchestration Prompt

```
I need you to execute the complete Requirements → Specification workflow for the requirement at {requirement_path}.

Follow these steps in order:

### Step 0: Pre-flight Validation

Verify prerequisites:
- [ ] Requirement file {requirement_path} exists
  - If not found, list available requirement files in docs/requirements/
  - Exit with helpful error message if missing
- [ ] Template file docs/templates/spec-template.md exists
- [ ] Output directory docs/specifications/ exists (create if missing)
- [ ] Output directory docs/diagrams/ exists (create if missing)
- [ ] Output directory docs/output-logs/ exists (create if missing)

If any critical prerequisite fails, report error and exit.

### Step 1: Generate Specification

Use the prompt at .github/prompts/generate-spec-from-requirement.prompt.md for {requirement_path}.

**Output**: `docs/specifications/spec_{req-name}.md`

Wait for completion before proceeding.

### Step 2: Create Architecture Diagram

Use the prompt at .github/prompts/create-architecture-diagram.prompt.md for the specification you just created.

**Important**: Architecture diagrams are created FROM the specification, showing the technical design.

**Output**: `docs/diagrams/architecture_{spec-name}.md`

Wait for completion before proceeding.

### Step 3: Create Threat Model

Use the prompt at .github/prompts/create-threat-model.prompt.md for the SPECIFICATION (not requirement) with scope: {per-specification | high-level-aggregate | grouped-by-feature}.

**Important**: Threat modeling requires the specification and architecture diagram to identify security risks based on actual system design, data flows, and integrations.

**Output**: `docs/diagrams/threat-model_{name}.md`

Wait for completion before proceeding.

### Step 4: Quality Review

Conduct a specification stage quality review following .github/instructions/quality-checklists.md (Specification Stage section).

Report results:
- ✅ Items that pass
- ❌ Items that fail (with details)
- 🟡 Items that need clarification

### Step 5: Documentation Update

Verify the following are updated:
- docs/SPEC-CROSS-REFERENCE.md
- docs/INDEX.md
- docs/specifications/spec_{name}.md
- docs/diagrams/threat-model_{name}.md
- docs/diagrams/architecture_{name}.md

### Step 6: Create Execution Log

Create an execution log following docs/rules/output-format.md in docs/output-logs/{timestamp}-spec-workflow.md including:
- All steps completed
- CodeGuard files referenced
- Quality review results
- Files created/updated
- Next steps

### Step 7: Report Summary

Provide a summary including:
- ✅ Success status
- 📁 Files created
- 🔒 CodeGuard rules applied
- 📋 Quality review results
- ⏳ Next step: Human review and approval

If quality review fails (❌), stop and request fixes before proceeding.
```

## 💡 Usage Examples

### With Claude Code

```
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-user-auth.md with threat model scope per-requirement
```

### With GitHub Copilot

```
@workspace I need to generate a complete specification from @docs/requirements/req-user-auth.md. Follow the workflow at @.github/prompts/workflow-requirements-to-spec.prompt.md including spec generation, threat model (per-requirement), architecture diagram, and quality review.
```

### Manual Step-by-Step

If you prefer to execute each step individually:

```
# Step 1
Use generate-spec-from-requirement prompt for docs/requirements/req-user-auth.md

# Step 2 (after Step 1 completes)
Use create-architecture-diagram prompt for docs/specifications/spec_user-auth.md

# Step 3 (after Step 2 completes)
Use create-threat-model prompt for docs/specifications/spec_user-auth.md with scope per-specification

# Step 4 (after Step 3 completes)
Conduct specification quality review using quality-checklists.md

# Step 5 (after Step 4 passes)
Verify documentation updates

# Step 6
Create execution log

# Step 7
Report summary
```

## 🚦 Decision Points

### Threat Model Scope

Choose based on requirement complexity:

- **per-requirement**: For individual feature requirements
- **high-level-aggregate**: For system-wide security view
- **grouped-by-feature**: For related requirements that form a module

### Quality Review Fails

If quality review identifies issues:

1. AI should attempt fixes if possible
2. Document issues in execution log
3. Request human guidance for ambiguous issues
4. Re-run quality review after fixes

### Approval Gate

After workflow completes:

- Human reviews generated specification, diagrams, and quality results
- If approved → Proceed to code generation workflow
- If rejected → Document feedback, make corrections, re-run quality review

## 📊 Expected Output

After successful completion:

```
✅ Requirements → Specification Workflow Complete

📁 Files Created:
- docs/specifications/spec_user-auth.md
- docs/diagrams/threat-model_user-auth.md
- docs/diagrams/architecture_user-auth.md
- docs/output-logs/2025-11-09-143022-spec-workflow.md

📝 Files Updated:
- docs/SPEC-CROSS-REFERENCE.md
- docs/INDEX.md
- docs/requirements/req_user-auth.md (added links)

🔒 CodeGuard Files Referenced:
- codeguard-0-authentication-mfa.instructions.md
- codeguard-0-input-validation-injection.instructions.md
- codeguard-0-session-management-and-cookies.instructions.md

📋 Quality Review: ✅ PASSED
- All specification stage checklist items verified
- Ready for human review

⏳ Next Step: Human review and approval before proceeding to code generation
```

## 🔗 Related Documentation

- [Master Workflow](../.github/instructions/master-workflow.md)
- [Generate Spec Prompt](generate-spec-from-requirement.prompt.md)
- [Create Threat Model Prompt](create-threat-model.prompt.md)
- [Create Architecture Diagram Prompt](create-architecture-diagram.prompt.md)
- [Quality Checklists](../.github/instructions/quality-checklists.md)
- [Output Format](../../docs/rules/output-format.md)

---

**TODO**: Add examples of handling common workflow issues and recovery strategies
