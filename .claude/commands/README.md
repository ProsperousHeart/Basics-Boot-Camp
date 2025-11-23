# Claude Code Slash Commands

This directory contains Claude Code-specific slash commands for this Python template repository.

## 🎯 Purpose

These slash commands are **convenience wrappers** that delegate to tool-agnostic workflow prompts in `.github/prompts/`. This design ensures:

- **Tool Agnostic**: Core workflows work with both Claude Code and GitHub Copilot
- **DRY Principle**: Single source of truth for workflow logic (in prompts)
- **Consistency**: Same workflow whether using slash commands or prompts directly
- **Maintainability**: Update prompts once, benefits all tools

## 📋 Available Commands

### Development Workflow Commands

| Command                                  | Purpose                                 | Delegates To                                                |
| ---------------------------------------- | --------------------------------------- | ----------------------------------------------------------- |
| `/setup-env`                             | Set up UV virtual environment           | `.github/instructions/uv-environment-setup.instructions.md` |
| `/create-requirement <name>`             | Create new requirement document         | `.github/prompts/create-requirement.prompt.md`              |
| `/make-spec-from-req <req-file> [scope]` | Generate specification from requirement | `.github/prompts/workflow-requirements-to-spec.prompt.md`   |
| `/implement-spec <spec-file>`            | Implement specification using TDD       | `.github/prompts/workflow-spec-to-code.prompt.md`           |
| `/quality-review`                        | Run comprehensive quality checks        | `.github/instructions/quality-checklists.md`                |

### Individual Operation Commands

| Command                                    | Purpose                                      | Delegates To                                             |
| ------------------------------------------ | -------------------------------------------- | -------------------------------------------------------- |
| `/create-architecture <spec-or-name>`      | Generate architecture diagram                | `.github/prompts/create-architecture-diagram.prompt.md`  |
| `/create-threat-model <spec> [scope]`      | Create security threat model (STRIDE)        | `.github/prompts/create-threat-model.prompt.md`          |
| `/verify <module-path>`                    | Comprehensive verification of implementation | `.github/prompts/verify-implementation.prompt.md`        |
| `/security-review <module-path>`           | Security review with CodeGuard              | `.github/prompts/security-review.prompt.md`              |
| `/update-docs <type> <files>`              | Update documentation indexes                | `.github/prompts/update-documentation.prompt.md`         |

### Command Details

#### `/setup-env`

Sets up or verifies the UV virtual environment.

**Usage:**

```
/setup-env
```

**What it does:**

- Checks for existing .venv
- Creates environment if needed
- Installs dependencies from requirements.txt and requirements-dev.txt
- Verifies installation

**Next step:** Create requirements or implement specs

---

#### `/create-requirement <name>`

Creates a new requirement document from the template.

**Usage:**

```
/create-requirement user-authentication
/create-requirement payment-processing
```

**What it does:**

- Uses template: `docs/templates/requirements-template.md`
- Creates: `docs/requirements/req_<name>.md`
- Updates cross-reference table and index

**Next step:** Use `/make-spec-from-req` to create specification

---

#### `/make-spec-from-req <req-file> [scope]`

Executes complete Requirements → Specification workflow.

**Usage:**

```
/make-spec-from-req docs/requirements/req_auth.md
/make-spec-from-req docs/requirements/req_auth.md high-level-aggregate
```

**Parameters:**

- `<req-file>`: Path to requirement document
- `[scope]`: Threat model scope (default: `per-requirement`)
  - `per-requirement` - Individual feature threat model
  - `high-level-aggregate` - System-wide security view
  - `grouped-by-feature` - Module-level threat model

**What it does:**

1. Generates specification from requirements
2. Creates threat model using STRIDE framework
3. Generates architecture diagram (Mermaid)
4. Runs quality review
5. Updates documentation (INDEX, SPEC-CROSS-REFERENCE)
6. Logs execution details

**Output:**

- `docs/specifications/spec_<name>.md`
- `docs/diagrams/threat-model_<name>.md`
- `docs/diagrams/architecture_<name>.md`
- `docs/output-logs/<timestamp>-spec-workflow.md`

**Next step:** Human review and approval, then use `/implement-spec`

---

#### `/implement-spec <spec-file>`

Implements specification using Test-Driven Development.

**Usage:**

```
/implement-spec docs/specifications/spec_user-auth.md
```

**What it does:**

1. Reviews specification and identifies features
2. Implements using TDD (RED-GREEN-REFACTOR for each function)
3. Applies CodeGuard security rules automatically
4. Runs security review
5. Runs quality validation (pytest, ruff, coverage)
6. Conducts post-test review
7. Updates documentation
8. Logs execution details

**TDD Process:**
For each function/method:

- 🔴 **RED**: Write failing test, verify it fails
- 🟢 **GREEN**: Write minimal code to pass, verify it passes
- 🔵 **REFACTOR**: Improve code, keep tests green

**Quality Requirements:**

- All tests pass: `pytest -v`
- Coverage ≥ 90%: `pytest --cov=src`
- Ruff checks pass: `ruff check src/ test/`
- Formatting applied: `ruff format src/ test/`
- Security review passes
- CodeGuard rules documented

**Output:**

- Source files in `src/`
- Test files in `test/` (mirroring `src/` structure)
- `docs/output-logs/<timestamp>-code-workflow.md`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`

**Next step:** Human code review and approval

---

#### `/create-architecture <spec-or-name>`

Generates an architecture diagram for a specification or component.

**Usage:**

```
/create-architecture docs/specifications/spec_user-auth.md
/create-architecture user-authentication
```

**What it does:**

- Reads specification and identifies architectural components
- Creates diagram in THREE required formats:
  - Text Description (bullet points/tables)
  - ASCII Diagram (text-based visual)
  - Mermaid Diagram (collapsible code block)
- Saves to `docs/diagrams/architecture_{name}.md`
- Updates documentation indexes

**Output:**

- `docs/diagrams/architecture_{name}.md` with all three formats
- Updated: `docs/INDEX.md`, `docs/SPEC-CROSS-REFERENCE.md`

**Next step:** Review diagram, create threat model if needed

---

#### `/create-threat-model <spec> [scope]`

Creates a security threat model using STRIDE framework.

**Usage:**

```
/create-threat-model docs/specifications/spec_user-auth.md
/create-threat-model docs/specifications/spec_api.md high-level-aggregate
```

**Parameters:**

- `<spec>`: Path to specification document
- `[scope]`: Threat model scope (default: `per-requirement`)
  - `per-requirement` - Individual feature threat model
  - `high-level-aggregate` - System-wide security view
  - `grouped-by-feature` - Module-level threat model

**What it does:**

1. Analyzes specification and architecture
2. Identifies assets, entry points, trust boundaries
3. Applies STRIDE framework (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege)
4. Documents threats, risks, and mitigations
5. References relevant CodeGuard guidelines
6. Updates documentation

**Output:**

- `docs/diagrams/threat-model_{name}.md`
- Updated: `docs/INDEX.md`, `docs/SPEC-CROSS-REFERENCE.md`

**Next step:** Review with security expert, implement mitigations

---

#### `/verify <module-path>`

Runs comprehensive verification of a Python module implementation.

**Usage:**

```
/verify src/auth/login.py
/verify src/utils/
```

**What it does:**

1. Import validation (dependencies declared)
2. Type checking (if mypy/pyright configured)
3. Test structure and quality (AAA pattern)
4. Test execution and coverage (≥ 90%)
5. Code quality (ruff linting and formatting)
6. Documentation (ABOUTME, docstrings, type hints)
7. Security (no hardcoded secrets, CodeGuard compliance)
8. Platform independence (path handling, test isolation)
9. UI/Accessibility (if UI components exist)
10. Integration (imports work, no breaking changes)

**Output:**

- Comprehensive pass/fail report with:
  - Overall verdict (✅ PASS or ❌ FAIL)
  - Results for each verification category
  - Specific issues with line numbers
  - Recommendations for improvement

**Next step:** If PASS: ready for review; If FAIL: address issues and re-verify

---

#### `/security-review <module-path>`

Conducts comprehensive security review of code implementation.

**Usage:**

```
/security-review src/auth/login.py
/security-review src/api/
```

**What it does:**

1. Identifies security context (reviews spec and threat model)
2. Applies CodeGuard rules (crypto, auth, input validation, etc.)
3. Checks OWASP Top 10 vulnerabilities
4. Reviews security test coverage
5. Generates detailed security report with severity levels

**Output:**

- Security review report with:
  - 🔴 Critical issues (must fix before deployment)
  - 🟡 Warnings (should address)
  - 🔵 Recommendations (best practices)
  - Overall verdict: ✅ SECURE / ⚠️ NEEDS FIXES / ❌ SECURITY ISSUES

**Next step:** Fix issues based on severity, re-review if critical issues found

---

#### `/update-docs <type> <files>`

Updates project documentation indexes and cross-references.

**Usage:**

```
/update-docs requirement docs/requirements/req_user-auth.md
/update-docs specification docs/specifications/spec_login.md
/update-docs implementation src/auth/login.py
/update-docs full-workflow docs/specifications/spec_user-auth.md
```

**Update Types:**

- `requirement` - New requirement added (status: 📝 Requirement Defined)
- `specification` - New spec created (status: 🔍 Specified)
- `implementation` - New code implemented (status: 🧪 In Development)
- `test` - New tests added (status: ✅ Complete)
- `diagram` - New diagram created
- `full-workflow` - Complete workflow completed

**What it does:**

- Updates `docs/SPEC-CROSS-REFERENCE.md` table
- Updates `docs/INDEX.md` sections
- Updates relevant README files
- Verifies all links are valid
- Generates update summary

**Output:**

- Updated documentation files
- Documentation Update Summary

**Next step:** Varies by update type

---

#### `/quality-review`

Runs comprehensive quality checks on current implementation.

**Usage:**

```
/quality-review
```

**What it does:**

1. Runs automated checks (pytest, coverage, ruff)
2. Reviews code quality (docstrings, standards)
3. Conducts security review (CodeGuard compliance)
4. Validates documentation completeness
5. Generates quality report

**Checks:**

- ✅ All tests pass
- ✅ Coverage ≥ 90%
- ✅ Ruff linting passes
- ✅ Docstrings follow standards
- ✅ No hardcoded credentials
- ✅ CodeGuard rules applied
- ✅ Documentation updated

**Output:**

- Quality report in terminal
- Coverage report: `htmlcov/index.html`
- List of issues and recommendations

**Next step:** Fix issues or proceed to approval

---

## 🔄 Relationship to Prompts

These slash commands are **thin wrappers** around workflow prompts:

```
.claude/commands/              →  Delegates to  →  .github/prompts/
├── setup-env.md               →                 →  (instructions)
├── create-requirement.md      →                 →  create-requirement.prompt.md
├── make-spec-from-req.md      →                 →  workflow-requirements-to-spec.prompt.md
├── implement-spec.md          →                 →  workflow-spec-to-code.prompt.md
├── quality-review.md          →                 →  quality-checklists.md
├── create-architecture.md     →                 →  create-architecture-diagram.prompt.md
├── create-threat-model.md     →                 →  create-threat-model.prompt.md
├── verify.md                  →                 →  verify-implementation.prompt.md
├── security-review.md         →                 →  security-review.prompt.md
└── update-docs.md             →                 →  update-documentation.prompt.md
```

**Why this design?**

1. **Single Source of Truth**: Workflow logic lives in prompts
2. **Tool Compatibility**: Prompts work with Claude AND Copilot
3. **Easy Maintenance**: Update prompt once, all tools benefit
4. **Flexibility**: Users can call prompts directly or use slash commands

## 🔧 For GitHub Copilot Users

Copilot users should reference prompts directly using `@workspace`:

```
@workspace Execute the workflow at @.github/prompts/workflow-requirements-to-spec.prompt.md for @docs/requirements/req-auth.md
```

See `.github/instructions/copilot-usage.instructions.md` for details.

## 📚 Related Documentation

- **Workflow Prompts**: `.github/prompts/` - Tool-agnostic prompt templates
- **Instructions**: `.github/instructions/` - Universal how-to guides
- **Master Workflow**: `.github/instructions/master-workflow.md`
- **Claude Usage**: `.github/instructions/claude-usage.instructions.md`
- **Copilot Usage**: `.github/instructions/copilot-usage.instructions.md`

## 📝 Creating New Commands

When adding new slash commands, **follow the Meta-Documentation Checklist** at `.github/META-CHECKLIST.md`.

Quick checklist:

1. Ensure there's a corresponding prompt in `.github/prompts/`
2. Keep commands as thin wrappers that delegate to prompts
3. Use parameter syntax: `{{$1}}` for required, `{{$2|default}}` for optional
4. Include usage examples and expected output
5. Document relationship to prompts
6. Update this README
7. Update `CLAUDE.md` slash commands table (if user-facing)
8. Test the command works before committing

**See `.github/META-CHECKLIST.md` for complete synchronization requirements.**

## 🗂️ Archive

The `.archive/` directory contains old commands that are not applicable to this Python template.

---

**Last Updated**: 2025-11-10