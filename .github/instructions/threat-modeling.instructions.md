# Threat Modeling Instructions

**Last Updated**: 2025-11-09

This document provides guidance for creating security threat models based on technical specifications.

## 🎯 Overview

Threat modeling helps identify potential security vulnerabilities during the design phase, after specifications are complete but before code is written. This proactive approach is more cost-effective than fixing security issues after implementation.

**CRITICAL**: Threat modeling must occur AFTER specifications are complete because you need to understand:
- System architecture and components
- Data flows and storage mechanisms
- Integration points and APIs
- Authentication and authorization approach
- Technology stack and deployment model

## 📋 When to Create Threat Models

Threat modeling occurs in Stage 4 of the development workflow (after specifications, before code).

Create threat models:
- **Per-Requirement**: For each individual requirement that involves security-sensitive operations
- **Per-Specification**: For each individual specification that involves security-sensitive operations
- **High-Level Aggregate**: Combining ALL specifications into a system-wide threat model
- **Grouped by Feature/Module**: For related specifications that form a cohesive feature

**Input Required**: Specification document and architecture diagrams

## 🔍 Threat Modeling Process

### Step 1: Identify Assets

What needs to be protected?
- User data
- Credentials and secrets
- API keys
- Business logic
- System resources

**TODO**: Add asset identification checklist

### Step 2: Identify Threat Actors

Who might attack the system?
- External attackers
- Malicious insiders
- Compromised accounts
- Automated bots

**TODO**: Add threat actor profiles and motivations

### Step 3: Identify Threats (STRIDE)

Use the STRIDE framework:

- **S**poofing: Impersonating users or systems
- **T**ampering: Modifying data or code
- **R**epudiation: Denying actions
- **I**nformation Disclosure: Exposing confidential data
- **D**enial of Service: Making systems unavailable
- **E**levation of Privilege: Gaining unauthorized access

**TODO**: Add STRIDE examples for common Python scenarios

### Step 4: Document Threats

Create a threat model document using Mermaid diagrams.

**TODO**: Add threat model template and examples

## 🎨 Creating Threat Model Diagrams with Mermaid

### Basic Threat Model Structure

```markdown
# Threat Model: {Feature Name}

**Requirement**: [REQ-XXX](../requirements/req-xxx.md)
**Date**: YYYY-MM-DD
**Status**: Draft | Under Review | Approved

## System Overview

[Describe the system or feature being modeled]

## Data Flow Diagram

\`\`\`mermaid
graph LR
    User[User] -->|HTTPS| WebApp[Web Application]
    WebApp -->|Encrypted| DB[(Database)]
    WebApp -->|API Call| ExtAPI[External API]
\`\`\`

## Threats Identified

### 1. [Threat Name]

- **Type**: STRIDE category
- **Threat Actor**: Who might exploit this?
- **Attack Vector**: How could they attack?
- **Impact**: What's the damage if successful?
- **Likelihood**: High | Medium | Low
- **Mitigation**: How to prevent/reduce risk?
- **CodeGuard Reference**: Relevant codeguard-*.instructions.md file

[Repeat for each threat]

## Trust Boundaries

\`\`\`mermaid
graph TB
    subgraph "Untrusted Zone"
        User[User]
        Internet[Internet]
    end

    subgraph "DMZ"
        WebApp[Web Application]
    end

    subgraph "Trusted Zone"
        DB[(Database)]
        Secrets[Secrets Manager]
    end

    User -->|HTTPS| WebApp
    WebApp -->|Encrypted| DB
    WebApp -->|IAM Auth| Secrets
\`\`\`

## Security Controls

| Control | Type | Status | CodeGuard Reference |
|---------|------|--------|---------------------|
| Input validation | Preventive | Planned | codeguard-0-input-validation-injection.instructions.md |
| [Add more controls] | | | |

## References

- **Cross-Reference**: [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)
- **Requirement**: [REQ-XXX](../requirements/req-xxx.md)
- **CodeGuard Files**: List relevant files
```

**TODO**: Add complete Mermaid diagram examples

## 📁 Output Location

Save threat models to:
- **Per-requirement**: `docs/diagrams/threat-model-{requirement-name}.md`
- **High-level aggregate**: `docs/diagrams/threat-model-system-overview.md`
- **Grouped by feature**: `docs/diagrams/threat-model-{feature-name}.md`

## ♻️ Diagram Versioning

**IMPORTANT**: When updating threat models, create a duplicate file with the new changes rather than editing the original. This preserves history and ensures IDE compatibility.

**Naming convention**:
```
threat-model-{name}-v1.md
threat-model-{name}-v2.md
threat-model-{name}-v3.md
```

Or use date:
```
threat-model-{name}-2025-11-09.md
threat-model-{name}-2025-12-15.md
```

**TODO**: Add versioning strategy and diff guidelines

## 🔒 CodeGuard Integration

Reference relevant CodeGuard instruction files for each identified threat:

| Threat Category | CodeGuard Reference |
|----------------|---------------------|
| Authentication | codeguard-0-authentication-mfa.instructions.md |
| Authorization | codeguard-0-authorization-access-control.instructions.md |
| SQL Injection | codeguard-0-input-validation-injection.instructions.md |
| Cryptography | codeguard-0-additional-cryptography.instructions.md, codeguard-1-crypto-algorithms.instructions.md |
| API Security | codeguard-0-api-web-services.instructions.md |
| Data Storage | codeguard-0-data-storage.instructions.md |
| Session Management | codeguard-0-session-management-and-cookies.instructions.md |

**TODO**: Add complete CodeGuard mapping table

## 🤖 AI Assistant Integration

### For Claude Code

When creating threat models:
1. Reference the requirement document
2. Apply STRIDE framework
3. Generate Mermaid diagrams
4. Link relevant CodeGuard files
5. Save to `docs/diagrams/`
6. Update cross-reference table

**TODO**: Add Claude-specific automation examples

### For GitHub Copilot

**TODO**: Add Copilot-specific examples

## ✅ Threat Model Quality Checklist

- [ ] All assets identified
- [ ] All threat actors considered
- [ ] STRIDE framework applied completely
- [ ] Data flow diagram created
- [ ] Trust boundaries clearly marked
- [ ] Each threat has mitigation strategy
- [ ] CodeGuard files referenced
- [ ] Linked to requirement document
- [ ] Added to cross-reference table

**TODO**: Expand checklist with specific criteria

## 📚 Related Documentation

- [Master Workflow](master-workflow.md)
- [Architecture Diagrams](architecture-diagrams.instructions.md)
- [Security Review](security-review.instructions.md)
- [CodeGuard Security Files](.) - All codeguard-*.instructions.md files

## 📝 Templates

### Threat Model Template

**TODO**: Create standalone threat model template file

### Quick Threat Assessment

**TODO**: Create quick assessment checklist for simple features

---

**TODO**: This is a placeholder. Expand with:
- Complete threat model examples
- STRIDE methodology deep-dive
- Common Python security threats
- Mermaid diagram gallery
- Automation scripts for threat model generation
- Integration with security review process
