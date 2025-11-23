# Prompt: Create Requirement Document

**Purpose**: Create a new requirement document from the project template
**Input**: Component/feature name (e.g., "user-authentication", "payment-processing")
**Output**: Requirement document in `docs/requirements/`
**References**:

- `docs/templates/requirements-template.md`
- `.github/instructions/master-workflow.md`

## Prompt

```
Create a new requirement document for: {component_name}

Follow these steps carefully:

### Step 1: Validate Prerequisites

- Verify docs/templates/requirements-template.md exists
  - If the template doesn't exist, inform the user and exit with a helpful error message
- Verify docs/requirements/ directory exists (create if missing)
- Check if docs/requirements/req_{component_name}.md already exists
  - If it exists, ask the user if they want to overwrite it or create a variant

### Step 2: Read Template

- **Read the full content of the requirement template** at docs/templates/requirements-template.md
- Understand the expected structure and all sections that need to be filled in

### Step 3: Create the Requirement Document

**Generate a requirement document** using the template structure with placeholders and guidance for each section:

- **Feature/Module Name**: Use {component_name} formatted appropriately
- **Context**: Purpose, role in application, users, usage scenarios
- **Functional Requirements**: Core features, business logic, state management
- **Interface Requirements**: Layout, visual design, interactive elements, responsive behavior, accessibility, module/package interface, CLI (if applicable), API endpoints (if applicable), UI (if applicable)
- **Data Requirements**: Data models and schemas, input/output specifications, storage requirements, API requirements, data validation
- **Integration Requirements - UI Front End**: Component dependencies, parent component integration, child components, page integration, progress tracking integration
- **Integration Requirements (Python Specific)**: Module dependencies, external service integrations, data flow, configuration requirements
- **Constraints**: Technical stack, performance requirements, design constraints, file structure & naming conventions, security considerations, browser & device support, platform & environment
- **Success Criteria**: Functional validation, UI/UX validation, integration validation, performance validation, technical validation, testing validation, security validation, documentation validation, deployment validation
- **Notes & Considerations**: Open questions, future enhancements, related specifications, risks and mitigation

Important considerations:
- Keep placeholders clear with brackets like [FeatureName], [Description]
- Add guidance comments where decisions are needed
- Flag security-sensitive areas that will need CodeGuard review
- Include reminders about CodeGuard rules in security sections
- Ensure all template sections are present

### Step 4: Save and Update Documentation

- Save the requirement document to docs/requirements/req_{component_name}.md
- Update docs/SPEC-CROSS-REFERENCE.md with new entry:
  - Add row with requirement file path
  - Leave specification, code, and test columns empty (to be filled later)
- Update docs/INDEX.md with link to new requirement under "Requirements" section
- Ensure proper formatting and markdown syntax throughout
- Validate all internal links

### Step 5: Confirm Completion

Report to the user:
- ✅ Requirement file created successfully at docs/requirements/req_{component-name}.md
- 📋 Brief description of what needs to be filled in
- 🔗 Links to updated documentation (cross-reference, index)
- ⏭️ Next step: Fill in the requirement details, then use the specification workflow to generate specs
```

## Example Usage

### With Claude Code

```
Execute the create-requirement prompt for user-authentication
```

Or using the slash command:

```
/create-requirement user-authentication
```

### With GitHub Copilot

```
@workspace Create a new requirement document for "payment-processing" using the template at @docs/templates/requirements-template.md. Update the cross-reference table and index.
```

## Expected Output

- New file: `docs/requirements/req_{component-name}.md`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Updated: `docs/INDEX.md`

## Next Steps

After creating the requirement:

1. **Fill in requirement details** - Work with stakeholders to complete all sections
2. **Review for completeness** - Ensure all sections are addressed
3. **Generate specification** - Use `/make-spec-from-req` or the workflow prompt to create technical specification

## Notes

- The created requirement document will contain the full template structure with placeholders
- Users should replace placeholders with actual requirements
- Security considerations should reference relevant CodeGuard instruction files
- The requirement serves as input for the specification generation workflow