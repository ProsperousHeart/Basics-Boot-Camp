Execute the prompt at `.github/prompts/create-requirement.prompt.md` for: {{$1}}

This command creates a requirement document following the project template structure.

**Usage:**

```
/create-requirement user-authentication
/create-requirement payment-processing
```

**What it does:**

1. Reads the template at `docs/templates/requirements-template.md`
2. Creates requirement file at `docs/requirements/req_{{$1}}.md`, which includes filling in the following but not limited to:

   - Overview (what problem this solves)
   - Functional Requirements (what it must do)
   - Non-Functional Requirements (performance, security, scalability)
   - Acceptance Criteria (measurable success criteria)
   - Dependencies (other requirements or systems)
   - Security Considerations (initial security thoughts)
   - Open Questions (items needing clarification)

3. Updates `docs/SPEC-CROSS-REFERENCE.md` and `docs/INDEX.md`

**Output:**

- `docs/requirements/req_{{$1}}.md` - New requirement document with template structure
- Updated: `docs/SPEC-CROSS-REFERENCE.md`, `docs/INDEX.md`

**Next Steps:**

1. Fill in the requirement details with actual specifications
2. Use `/make-spec-from-req` to generate technical specification

**Note:** This command delegates to the tool-agnostic prompt at `.github/prompts/create-requirement.prompt.md`