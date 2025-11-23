# Prompt: Create Threat Model

**Purpose**: Generate security threat model based on a specification
**Input**: Specification document path, scope (per-requirement | per-specification | high-level-aggregate | grouped-by-feature)
**Output**: Threat model diagram in `docs/diagrams/`
**Prerequisites**: Specification and architecture diagram must exist
**References**:
- `.github/instructions/threat-modeling.instructions.md`
- Relevant CodeGuard instruction files

## Prompt

```
Create a security threat model for the specification at {specification_path}.

**IMPORTANT**: Threat modeling requires a completed specification and architecture diagram. Verify these exist before proceeding.

Scope: {per-requirement | per-specification | high-level-aggregate | grouped-by-feature}

Instructions:
0. Read the requirements document and if it is not found in {specification_path}, return an error indicating the file is missing. When the specification is made, it should include the requirements document it was designed from.
1. Read the specification document at {specification_path}
2. Read the architecture diagram at docs/diagrams/architecture_{name}.md
3. Follow threat modeling process in .github/instructions/threat-modeling.instructions.md
3. Apply STRIDE framework:
   - Spoofing
   - Tampering
   - Repudiation
   - Information Disclosure
   - Denial of Service
   - Elevation of Privilege
4. Create Mermaid diagrams showing:
   - Data flow diagram
   - Trust boundaries
   - Threat actors and attack vectors
5. For each identified threat:
   - Classify by STRIDE category
   - Assess impact and likelihood
   - Propose mitigation
   - Reference relevant CodeGuard instruction file
6. Save to docs/diagrams/threat-model-{name}.md
7. Update docs/SPEC-CROSS-REFERENCE.md
8. Log execution details to docs/output-logs/{timestamp}-threat-modeling.md

Note: When updating existing threat models, create a new version file (threat-model-{name}-v2.md) rather than editing the original.
```

## Example Usage

### With Claude Code

```
# Per Requirement
Use the create-threat-model prompt for docs/requirements/req_plant-database.md with scope per-requirement

# Per Specification
Use the create-threat-model prompt for docs/specifications/spec_auth.md with scope per-specification
```

### With GitHub Copilot

```
# Per Specification
@workspace Create a threat model for @docs/specifications/spec_auth.md (using the existing architecture diagram) following @.github/instructions/threat-modeling.instructions.md with STRIDE framework and Mermaid diagrams.
```

## Expected Output

- Threat model: `docs/diagrams/threat-model-{name}.md`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Log: `docs/output-logs/{timestamp}-threat-modeling.md`

**TODO**: Add complete threat model example with STRIDE analysis
