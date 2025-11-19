Execute the documentation update prompt at `.github/prompts/update-documentation.prompt.md`

Update type: {{$1}}
Files: {{$2}}

This command updates project documentation indexes and cross-references.

**Usage:**

```
/update-docs requirement docs/requirements/req_user-auth.md
/update-docs specification docs/specifications/spec_login.md
/update-docs implementation src/auth/login.py
/update-docs full-workflow docs/specifications/spec_user-auth.md
```

**Update Types:**

- **requirement** - New requirement added
- **specification** - New specification created
- **implementation** - New code implemented
- **test** - New tests added
- **diagram** - New diagram created
- **full-workflow** - Complete workflow completed

**What it does:**

1. **Updates SPEC-CROSS-REFERENCE.md**: Adds/updates entry with appropriate status
2. **Updates INDEX.md**: Adds entry to appropriate section (requirements/specs/implementations/diagrams)
3. **Updates README files**: Updates docs/requirements/, docs/specifications/, docs/diagrams/ README files
4. **Verifies Links**: Ensures all links are valid and bidirectional where appropriate
5. **Generates Summary**: Reports what was updated

**Status Values:**

- 📝 **Requirement Defined** - Requirement exists, no spec yet
- 🔍 **Specified** - Specification created, not implemented
- 🧪 **In Development** - Implementation in progress
- ✅ **Complete** - Fully implemented and tested
- 🚀 **Deployed** - In production

**Files Updated:**

- `docs/SPEC-CROSS-REFERENCE.md`
- `docs/INDEX.md`
- `docs/{category}/README.md` (as appropriate)

**Output:**

- Documentation Update Summary showing:
  - Files updated
  - Changes made
  - New entries added
  - Status updates
  - Link verification results
  - Next steps

**Verification Checks:**

- ✅ All links validated
- ✅ Formatting consistent
- ✅ Alphabetical order maintained
- ✅ No duplicate entries

**Next Steps:**

Varies by update type - summary will indicate what should happen next

**Note:** This command delegates to the tool-agnostic prompt at `.github/prompts/update-documentation.prompt.md`