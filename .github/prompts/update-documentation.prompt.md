# Prompt: Update Documentation

**Last Updated**: 2025-11-10

**Purpose**: Update project documentation indexes and cross-references
**Input**: Type of update and relevant file paths
**Output**: Updated INDEX.md, SPEC-CROSS-REFERENCE.md, and other documentation
**References**: N/A

## Prompt

```
You are updating project documentation for: {update_type}

**Update Type**: {update_type}
- "requirement" - New requirement added
- "specification" - New specification created
- "implementation" - New code implemented
- "test" - New tests added
- "diagram" - New diagram created
- "full-workflow" - Complete workflow completed

**Files involved**:
{list_of_files}

## Step 1: Update SPEC-CROSS-REFERENCE.md

Read `docs/SPEC-CROSS-REFERENCE.md` and update the table:

### Table Format
```markdown
| Requirement | Specification | Implementation | Tests | Status |
|-------------|---------------|----------------|-------|--------|
| [REQ-XXX](requirements/req_{name}.md) | [SPEC-XXX](specifications/spec_{name}.md) | `src/{module}/` | `test/test_{module}.py` | {status} |
```

### Status Values
- 📝 **Requirement Defined** - Requirement exists, no spec yet
- 🔍 **Specified** - Specification created, not implemented
- 🧪 **In Development** - Implementation in progress
- ✅ **Complete** - Fully implemented and tested
- 🚀 **Deployed** - In production

### Actions by Update Type

**For "requirement"**:
- Add new row with requirement link
- Set status to "📝 Requirement Defined"
- Leave spec, implementation, and tests empty

**For "specification"**:
- Find matching requirement row
- Add specification link
- Add architecture diagram link if exists
- Add threat model link if exists
- Update status to "🔍 Specified"

**For "implementation"**:
- Find matching spec row
- Add implementation path
- Update status to "🧪 In Development"

**For "test"**:
- Find matching implementation row
- Add test file path
- Update status to "✅ Complete"

**For "diagram"**:
- Find matching row
- Add diagram link to appropriate column
- Don't change status

**For "full-workflow"**:
- Add/update entire row with all information
- Set status to "✅ Complete"

## Step 2: Update INDEX.md

Read `docs/INDEX.md` and update appropriate sections:

### Sections to Update

**Requirements** section:
```markdown
### Requirements
- [REQ-{ID}]({name}) - {brief description} ({date})
```

**Specifications** section:
```markdown
### Specifications
- [SPEC-{ID}]({name}) - {brief description} ({date})
  - Architecture: [diagram](diagrams/architecture_{name}.md)
  - Threat Model: [model](diagrams/threat-model_{name}.md)
```

**Implementations** section (if applicable):
```markdown
### Implementations
- **{module_name}** (`src/{path}/`) - {brief description}
  - Tests: `test/test_{name}.py`
  - Coverage: {X}%
```

**Diagrams** section (if applicable):
```markdown
### Diagrams
- [Architecture: {name}](diagrams/architecture_{name}.md) - {description}
- [Threat Model: {name}](diagrams/threat-model_{name}.md) - {description}
```

### Actions
1. Add entry to appropriate section(s)
2. Keep entries sorted by date (newest first within sections)
3. Use consistent formatting
4. Include brief description (1 line max)
5. Link to files using relative paths

## Step 3: Update README Files

Update relevant README files:

### docs/requirements/README.md
If new requirement added:
- Add to the requirements list
- Keep alphabetical order

### docs/specifications/README.md
If new specification added:
- Add to the specifications list
- Keep alphabetical order

### docs/diagrams/README.md
If new diagram added:
- Add to appropriate category (architecture/threat-model/other)
- Keep alphabetical order

## Step 4: Verify All Links

Check that all links in updated files are valid:

1. **Internal links**: Verify files exist
2. **Relative paths**: Ensure correct path structure
3. **Markdown links**: Proper syntax `[text](path)`
4. **Bidirectional links**: If A links to B, consider if B should link to A

## Step 5: Generate Update Summary

Create a summary of changes:

### Documentation Update Summary

**Update Type**: {update_type}
**Date**: {timestamp}

**Files Updated**:
- ✅ `docs/SPEC-CROSS-REFERENCE.md`
- ✅ `docs/INDEX.md`
- ✅ `docs/{category}/README.md` (if applicable)

**Changes Made**:
1. {description of change 1}
2. {description of change 2}
...

**New Entries**:
- {file or section}: {entry added}

**Status Updates**:
- {REQ-XXX}: {old status} → {new status}

**Verification**:
- ✅ All links validated
- ✅ Formatting consistent
- ✅ Alphabetical order maintained
- ✅ No duplicate entries

**Next Steps**:
{what should happen next, if anything}
```

## Important Guidelines

- **Be consistent**: Follow existing formatting exactly
- **Be complete**: Update all relevant files, not just one
- **Be accurate**: Verify file paths before adding links
- **Be organized**: Maintain alphabetical/chronological order
- **Be clear**: Use descriptive brief descriptions

## Example Usage

### With Claude Code

```
Execute the update-documentation prompt for requirement "user-auth"
Execute the update-documentation prompt after completing implementation of spec_login.md
```

### With GitHub Copilot

```
@workspace Update documentation for the new requirement at @docs/requirements/req_user-auth.md following @.github/prompts/update-documentation.prompt.md
```

### As part of workflow

```
After creating specification, update documentation before moving to implementation.
After completing TDD implementation, update documentation with implementation and test paths.
```

## Expected Output

Updated documentation files showing:
- New/updated entries in SPEC-CROSS-REFERENCE.md
- New/updated entries in INDEX.md
- Updated README files
- Validation that all links work
- Summary of changes made

---

**Related Documentation**:
- [Master Workflow](../.github/instructions/master-workflow.md)
- [Markdown Standards](../../docs/rules/markdown-standards.md)