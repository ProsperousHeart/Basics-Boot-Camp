Execute the complete Specification → Code workflow using Test-Driven Development for the specification at: {{$1}}

This command orchestrates the full TDD implementation workflow including:
1. Review specification and identify features to implement
2. TDD implementation (RED-GREEN-REFACTOR cycles for each function)
3. Security review with CodeGuard compliance
4. Quality validation (pytest, ruff, coverage)
5. Post-test review
6. Documentation updates
7. Execution logging

Follow the workflow prompt at .github/prompts/workflow-spec-to-code.prompt.md

**Usage:**
- /implement-spec docs/specifications/spec_user-auth.md

**TDD Process:**
For EACH function/method:
1. 🔴 RED: Write failing test, verify it fails
2. 🟢 GREEN: Write minimal code to pass, verify it passes
3. 🔵 REFACTOR: Improve code, keep tests green

**Expected Output:**
- Source files in src/
- Test files in test/ (mirroring src/ structure)
- docs/output-logs/{timestamp}-code-workflow.md
- Updated: docs/SPEC-CROSS-REFERENCE.md

**Quality Requirements:**
- All tests pass (pytest -v)
- Coverage ≥ 90% (pytest --cov=src)
- Ruff checks pass (ruff check src/ test/)
- Formatting applied (ruff format src/ test/)
- Security review passes
- CodeGuard rules applied and documented

**Next Step:** Human code review and approval