Execute the threat model creation prompt at `.github/prompts/create-threat-model.prompt.md` for: {{$1}}

Scope: {{$2|per-requirement}}

This command creates a security threat model using the STRIDE framework.

**Usage:**

```
/create-threat-model docs/specifications/spec_user-auth.md
/create-threat-model docs/specifications/spec_api.md high-level-aggregate
/create-threat-model user-authentication grouped-by-feature
```

**Scope Options:**

- **per-requirement** (default) - Individual feature threat model
- **high-level-aggregate** - System-wide security view
- **grouped-by-feature** - Module-level threat model

**What it does:**

1. Reads specification and architecture diagram
2. Identifies assets, entry points, and trust boundaries
3. Applies STRIDE framework:
   - **S**poofing
   - **T**ampering
   - **R**epudiation
   - **I**nformation Disclosure
   - **D**enial of Service
   - **E**levation of Privilege
4. Creates threat model document
5. Links to relevant CodeGuard guidelines
6. Saves to `docs/diagrams/threat-model_{name}.md`
7. Updates documentation indexes

**STRIDE Framework:**

- **Spoofing**: Impersonating users, systems, or processes
- **Tampering**: Modifying data or code
- **Repudiation**: Denying actions without proof
- **Information Disclosure**: Exposing sensitive information
- **Denial of Service**: Making system unavailable
- **Elevation of Privilege**: Gaining unauthorized access

**Output:**

- `docs/diagrams/threat-model_{name}.md` with:
  - System overview
  - Assets and entry points
  - Trust boundaries
  - STRIDE analysis
  - Threat scenarios
  - Mitigations
  - CodeGuard references
- Updated `docs/INDEX.md`
- Updated `docs/SPEC-CROSS-REFERENCE.md`

**Threat Model Structure:**

```markdown
# Threat Model: {Name}

## System Overview
{Description and scope}

## Assets
- {Asset 1}: {description}
- {Asset 2}: {description}

## Entry Points
- {Entry point 1}: {description}
- {Entry point 2}: {description}

## Trust Boundaries
{Diagram or description}

## STRIDE Analysis

### Spoofing
- **Threat**: {description}
  - **Likelihood**: High/Medium/Low
  - **Impact**: High/Medium/Low
  - **Mitigation**: {how to prevent}
  - **CodeGuard Reference**: {file}

### Tampering
...

## Threat Scenarios
{Specific attack scenarios}

## Recommended Mitigations
{Prioritized list of security controls}
```

**Risk Levels:**

- **Critical**: High likelihood + High impact
- **High**: High likelihood OR High impact
- **Medium**: Medium likelihood + Medium impact
- **Low**: Low likelihood + Low impact

**Next Steps:**

After creating threat model:
1. Review with security expert (if available)
2. Implement mitigations in specification
3. Verify mitigations during implementation
4. Add security tests for identified threats

**Note:** This command delegates to the tool-agnostic prompt at `.github/prompts/create-threat-model.prompt.md`