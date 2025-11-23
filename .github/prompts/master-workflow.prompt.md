# Master Testing Workflow Prompt - ALWAYS USE THIS

---

mode: ask
trigger: "write unit tests for <component/module_name>"
title: "Automated Test Generation Workflow"
priority: highest
description: |
This is the master prompt to execute the automated test generation workflow. It must be executed first whenever the user requests unit tests for a component or module. Follow the detailed instructions in the referenced workflow definition file to complete all steps in order.

---

## Critical Instructions

When user requests test generation using ANY of these commands:

```
write unit tests for <component/module_name>
create tests for <component/module_name>
write integration tests for <component/module_name>
write acceptance tests for <component/module_name>
generate unit tests for <component/module_name>
test <component/module_name>
```

**YOU MUST:**

1. **IMMEDIATELY load this Master Testing Workflow file:**

   - `.github/instructions/master-workflow.md`

2. **FOLLOW the workflow EXACTLY as specified:**

   - Execute steps 0-7 in sequential order
   - Use the exact output format specified
   - Follow all file references in the correct order

3. **NEVER skip or modify the workflow sequence:**

   - Steps 0-4: Development Phase (use `testcase.instructions.md` and `testcase.prompt.md`)
   - Step 5: Quality Review Phase (use `post-test-review.md`)
   - Step 6: Security Review Phase (use `security-review.md`)
   - Step 7: Final Validation & Conclusion

4. **Output format MUSt start with:**

   ```
   =========================================
   AUTOMATED TEST GENERATION WORKFLOW OUTPUT
   =========================================

   [Your detailed output here following the workflow steps]
   ```

---

## File Loading Sequence (MANDATORY)

### Phase 1: Load Master Workflow

```
Load:  .github/instructions/master-workflow.md
Purpose:  Understand complete workflow architecture
Action:  Read entire file to understand steps 0-7
```

### Phase 2: Load Development Instructions

```
Load:  .github/instructions/testcase.instructions.md
Load:  .github/prompts/testcase.prompt.md
Purpose:  Execute steps 0-4 (Development Phase)
```

### Phase 3: Load Error Resolution Knowledge Base (On Demand)

```
Load:  .github/instructions/error-resolution-kb.md
Purpose:  Understand error resolution procedures & resolve during development phase
Trigger:  ANY error occurred
```

### Phase 4: Load Quality Review Instructions (After User Confirmation)

```
Load:  .github/instructions/post-test-review.md
Purpose:  Understand and execute step 5 (quality review phase)
Trigger:  User confirms "yes" to proceed to review
```

### Phase 5: Load Security Review Instructions (After Quality Review)

```
Load:  .github/instructions/security-review.md
Purpose:  Understand and execute step 6 (security review phase)
Trigger:  Quality review is complete & all quality checks passed
```

---

## Workflow Execution Rules

### Rule 1: Always Start With STEP 0

**Output:**

```
STEP 0:  WORKFLOW INITIALIZATION
    Phase 0.1:  Loading workflow configuration
    Phase 0.2:  Validating workspace structure
    Phase 0.3:  Loading primary instruction files
        🗸 Loaded:  .github/instructions/testcase.instructions.md
        🗸 Loaded:  .github/prompts/testcase.prompt.md
        🗸 Loaded:  .github/instructions/error-resolution-kb.md
    Phase 0.4:  Workflow initialization complete
```

### Rule 2: Never Skip User Confirmation

**MANDATORY at end of Step 4:**

```
══════════════════════════════════════════════════════
USER CONFIRMATION REQUIRED
══════════════════════════════════════════════════════

Development phase complete. Ready to proceed to quality review.

Do you want to proceed to the Quality Review Phase? (yes/no)
```

**IF NO:** Stop and await user isntructions
**IF YES:** Proceed to Step 5

### Rule 3: Iterate Reviews Until Pass

**Step 5 Loop:**

```
WHILE (post-test-review.md indicates issues)
    Execute checks -> Identify failures -> Fix -> Re-run -> repeat
```

**STEP 6 Loop:**

```
WHILE (security-review.md indicates issues)
    Execute security checks -> Identify gaps -> Add tests -> Re-run -> repeat
```

### Rule 4: Always Conclude with Step 7

**Output:**

```
STEP 7:  FINAL VALIDATION & CONCLUSION
    Phase 7.1:  Validate all tests (comprehensive)
    Phase 7.2:  Workflow step verification
    Phase 7.3:  File Modification Verification
    Phase 7.4:  Documentation Verification
    Phase 7.5:  Compliance Verification

══════════════════════════════════════════════════════
AUTOMATED TEST GENERATION WORKFLOW - COMPLETE
══════════════════════════════════════════════════════

[complete summary with all statistics and results]
```

---

## Output Format Requirements

### Step Format (Use for ALL Steps 0-7)

```
STEP <N>:  <STEP NAME>
  Phase <N>.<M>:  <PHASE NAME>
    🗸 <Action Completed>
    ⚠ <Warning or Issue>
    ✗ <Failure - will be fixed>
    ➔ <Next Action>
```

### Phase Format (Use within each Step)

```
Phase <N>.<M>:  <PHASE NAME>
  🗸 <Detailed action with result>
```

### Success Indicators

- 🗸 (checkmark) = Action completed successfully
- ✅ (checkbox) major milestone achieved
- ⚠ (warning) = Non-critical issue detected
- ✗ (cross) = Critical failure detected

--

## Checkpoint Formats

### Coverage Checkpoint (Step 3)

```
══════════════════════════════════════════════════════
COVERAGE CHECKPOINT
══════════════════════════════════════════════════════

Current Coverage:  <percentage>%
Required Coverage:  80%

Would you like to retry to improve coverage? (yes/no)
```

### Review Checkpoint (End of Step 4)

```
════════════════════════════════════════════════════
REVIEW CHECKPOINT - USER CONFIRMATION REQUIRED
──────────────────────────────────────────────────────

Development phase complete. Ready to proceed to quality review.

Would you like to proceed to the Quality Review Phase? (yes/no)
```

---

## Error Handling During Workflow

### IF Error in Steps 0-4:

1. Log: "Error encountered in Step <N>, Phase <M>: <error details>"
2. Log: "Consulting Error Resolution Knowledge Base..."
3. Load: `.github/instructions/error-resolution-kb.md`
4. Search for matching pattern
5. Apply recommended resolution
6. Re-attempt failed action
7. If still fails, escalate to user with detailed error report. Otherwise continue workflow.

### IF Error in Step 5:

1. Log: "Quality Review failed: <issue details>"
2. Identify specific check that failed
3. Modify test files to fix issue OR make suggestion in chat for how source code could be improved
4. Re-run post-test-review.md checks
5. Repeat until all checks pass

### IF Error in Step 6:

1. Log: "Security Review failed: <issue details>"
2. Identify specific security gap
3. Add necessary tests to cover gap OR make suggestion in chat for how source code could be improved
4. Re-run security-review.md checks
5. Repeat until all checks pass

---

## Success Criteria Before Conclusion

**Before outputting "WORKFLOW COMPLETE", verify:**

- ✅ All steps 0-7 executed in order
- ✅ All phases within each step completed
- ✅ Development complete (100% covverage, all tests pass)
- ✅ Quality review passed (post-test-review.md)
- ✅ Security review passed (security-review.md)
- ✅ Final validation checks complete
- ✅ All outputs formatted correctly
- ✅ Source files unchanged (only test files modified)
- ✅ Documentation complete

**IF ANY criteria NOT met, do not conclude workflow.**

---

## Common Mistakes To Avoid

```
# Missing Steps 0-1
STEP 2: TEST GENERATION  # ❌ WRONG
```

### ✅ CORRECT: Following complete sequence

```
STEP 0:  WORKFLOW INITIALIZATION
  Phase 0.1:  Loading workflow configuration
  ...

STEP 1:  ENVIRONMENT SETUP & DISCOVERY
  PHase 1.1:  Virtual environment detection
  ...

STEP 2:  TEST GENERATION
  Phase 2.0:  Analyzing component/module
  Phase 2.1:  Test structure activation
  ...
```

---

### ❌ WRONG: Proceeding to review without user confirmation

```
STEP 4:  ERROR RESOLUTION & COVERAGE IMPROVEMENT
  🗸 Coverage: 100%

STEP 5:  Quality REVIEW PHASE  # ❌ WRONG - MISSING USER CONFIRMATION
```

### ✅ CORRECT: Always ask for confirmation

```
STEP 4:  ERROR RESOLUTION & COVERAGE IMPROVEMENT
  🗸 Coverage: 100%

════════════════════════════════════════════════════
REVIEW CHECKPOINT - USER CONFIRMATION REQUIRED
════════════════════════════════════════════════════

Errors resolved and coverage updated.

Shall we move ahead to review? (yes/no)

[Wait for user response]

STEP 5:  QUALITY REVIEW PHASE  # 🗸 only after "yes"
```

### ❌ WRONG: Stopping at Step 5 without security review

```
STEP 5:  QUALITY REVIEW PHASE
  🗸 All quality checks passed

WORKFLOW COMPLETE  # ❌ WRONG - MISSING STEP 6 & 7
```

### ✅ CORRECT: Always complete all steps

```
STEP 5:  QUALITY REVIEW PHASE
  🗸 All quality checks passed

STEP 6:  SECURITY REVIEW PHASE
  🗸 All security checks passed

STEP 7:  FINAL VALIDATION CHECKS
  🗸 All validation checks passed

AUTOMATED TEST GENERATION WORKFLOW - COMPLETE
```

---

### ❌ WRONG: Not iterating on review failures

```
STEP 5:  QUALITY REVIEW PHASE
  ✗ Missing edge case tests
  ✗ Platform independence check failed

STEP 6:  SECURITY REVIEW PHASE  # ❌ WRONG - SKIPPING RE-ITERATION
```

### ✅ CORRECT: Always iterate until pass

```
STEP 5:  QUALITY REVIEW PHASE
  ✗ Missing edge case tests
    ➔ Fixing: Added edge case tests for null inputs
  🗸 Re-running quality checks
  ✗ Platform independence check failed
    ➔ Fixing: Replaced hard coded paths with OS-agnostic methods
  🗸 Re-running quality checks
  🗸 All quality checks passed  # now can proceed
```

---

## Quick Reference Checklist

Before starting workflow:

- [ ] Load master-workflow.md
- [ ] Load testcase.instructions.md
- [ ] Load testcase.prompt.md
- [ ] Ready to execute Step 0

During development (Steps 0-4):

- [ ] Virtual environment activated
- [ ] Reference source code to be analyzed
- [ ] Generate tests per instructions using proven patterns
- [ ] Monitor coverage after test generation to get 100% coverage
- [ ] Handle errors using error-resolution-kb.md as needed

Before proceeding to review:

- [ ] User confirmed "yes" to proceed to quality review
- [ ] All development criteria met

During quality review (Step 5):

- [ ] Loaded post-test-review.md
- [ ] Execute all automated quality checks
- [ ] Fixed all failures
- [ ] Re-validate until all checks pass

During security review (Step 6):

- [ ] Loaded security-review.md
- [ ] Execute all automated security checks
- [ ] Add required security tests
- [ ] Re-validate until all checks pass

Before concluding workflow (Step 7):

- [ ] All steps 0-7 executed
- [ ] All phases complete
- [ ] Final validation passed
- [ ] Summary statistics prepared

---

## Final Reminder

**THIS PROMPT IS MANDATORY**

Every test generation request MUST:

1. Load and follow master-workflow.md
2. Execute steps 0-7 in order
3. Format output exactly as required
4. Reference correct instruction files at each step
5. Iterate reviews until all checks pass
6. Complete with comprehensive summary

**NO EXCEPTIONS. NO SHORTCUTS. FOLLOW THE WORKFLOW.**

---

This prompt ensures consistent, high-quality automated test generation with comprehensive validation at every stage across all components and modules in the repository.
