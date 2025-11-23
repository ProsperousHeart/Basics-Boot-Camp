Execute the complete Requirements → Specification workflow for the requirement document at: {{$1}}

This command orchestrates the full workflow including:

1. Specification generation from requirements
2. Threat model creation (per-requirement scope)
3. Architecture diagram generation
4. Quality review
5. Documentation updates (INDEX, SPEC-CROSS-REFERENCE)
6. Execution logging

Follow the workflow prompt at .github/prompts/workflow-requirements-to-spec.prompt.md

Use threat model scope: {{$2|per-requirement}}

**Usage:**

- /make-spec-from-req docs/requirements/req_auth.md
- /make-spec-from-req docs/requirements/req_auth.md high-level-aggregate
- /make-spec-from-req docs/requirements/req_auth.md grouped-by-feature

**Expected Output:**

- docs/specifications/spec\_{name}.md
- docs/diagrams/threat-model\_{name}.md
- docs/diagrams/architecture\_{name}.md
- docs/output-logs/{timestamp}-spec-workflow.md
- Updated: docs/SPEC-CROSS-REFERENCE.md, docs/INDEX.md

**Next Step:** Human review and approval before implementing code
