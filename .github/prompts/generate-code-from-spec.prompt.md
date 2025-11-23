# Prompt: Generate Code from Specification

**Purpose**: Generate production code from a specification using TDD
**Input**: Specification document path
**Output**: Source code in `src/`, tests in `test/`
**References**:
- `.github/instructions/tdd-workflow.instructions.md`
- `.github/instructions/master-workflow.md`
- Relevant CodeGuard instruction files
- `docs/rules/docstring-standards.md`

## Prompt

```
Implement the specification at {specification_path} using Test-Driven Development (TDD).

Follow these steps carefully and iteratively refine until all acceptance criteria are met:

## Step 1: Read and Parse Specification

1. **Read the specification file**: Read the full content of {specification_path}
   - If the file doesn't exist, inform the user and suggest available spec files in docs/specifications/
   - Parse the specification sections: Context, Requirements, Constraints, Acceptance Criteria

2. **Extract implementation details**:
   - Module/package/class names from the spec
   - File paths where code should be created (look in Constraints > Technical Constraints)
   - Function/class signatures and interfaces
   - Data models and types needed
   - Integration points with existing code
   - **Security considerations:**
     - Identify relevant CodeGuard files from security constraints
     - Note authentication/authorization requirements
     - Identify sensitive data handling needs
     - Note input validation requirements
     - Identify cryptographic operations
     - Document threat model mitigations needed

3. **Create implementation plan**:
   - List all functions/classes to implement
   - Identify test scenarios from acceptance criteria
   - Determine implementation order (dependencies first)
   - Note performance requirements
   - Identify edge cases to handle

4. **Create test plan for user approval**:
   - For EACH function/class, list:
     - Functional tests needed (expected behaviors)
     - Security tests needed (input validation, injection prevention, auth/authz, etc.)
     - Edge case tests
     - Error condition tests
   - Present test plan to user with format:
     ```
     Test Plan for {module_name}:

     Function: {function_name}
     - Functional Tests:
       - test_{behavior_1}: {description}
       - test_{behavior_2}: {description}
     - Security Tests:
       - test_{security_aspect_1}: {description}
       - test_{security_aspect_2}: {description}
     - Edge Cases:
       - test_{edge_case_1}: {description}

     [Repeat for each function/class]
     ```
   - **WAIT FOR USER APPROVAL** before proceeding to implementation
   - User may request additions, removals, or modifications to test plan

## Step 2: Implement Using TDD (RED-GREEN-REFACTOR)

**IMPORTANT**: Do not begin implementation until user approves the test plan from Step 1.

Follow the TDD workflow at .github/instructions/tdd-workflow.instructions.md strictly.

For EACH function/class/feature:

### 🔴 RED: Write Failing Test First

**Security is continuous, not a phase. Follow shift-left approach:**

1. Create test file in test/ (mirroring src/ structure)
2. Write functional test that defines expected behavior (standard unit test)
3. Run test: `pytest test/test_{module}.py::test_{function} -v`
4. Verify test FAILS for the right reason (not syntax error)
5. **BEFORE implementing, add security-specific tests:**
   - Input validation tests (boundary conditions, type validation, format, null/undefined handling)
   - Injection prevention tests (XSS payloads, SQL injection patterns, command injection, path traversal)
   - Authentication/authorization tests (permission checks, role validation)
   - Cryptographic operation tests (if applicable)
   - Sensitive data handling tests (no leakage in logs/errors)
6. Run all tests: `pytest test/test_{module}.py -v`
7. Verify ALL tests FAIL (functional + security)
8. Report: Test name, expected behavior, security tests added

### 🟢 GREEN: Write Code to Pass ALL Tests

**Code must pass BOTH functional AND security tests.**

1. Create/update source file in src/
2. Write minimal code to pass ALL tests (functional + security, no over-engineering)
3. Apply project patterns:
   - Use type hints for all parameters and return values
   - Add ABOUTME comment (2 lines) if new module
   - Import required dependencies
4. **Use secure coding practices** (not optional):
   - Input validation and sanitization (prevent injection attacks)
   - Whitelist validation (not blacklist)
   - Parameterized queries (prevent SQL injection)
   - Established security libraries (bcrypt, not custom crypto)
   - Fail securely (deny by default)
   - Defense in depth (multiple validation layers)
   - Principle of least privilege
   - No hardcoded secrets/credentials
5. Handle error cases securely (no sensitive data leakage)
6. Run all tests: `pytest test/test_{module}.py -v`
7. Verify ALL tests PASS (functional + security)
8. Report: Code added, all tests passing, secure coding practices applied

### 🔵 REFACTOR: Improve Code

1. Improve code while keeping tests green:
   - Add comprehensive docstring (Google style from docs/rules/docstring-standards.md)
   - Improve variable/function names
   - Remove duplication
   - Add defensive coding (input validation, error handling)
   - Optimize if needed (performance requirements from spec)
2. Run all tests: `pytest test/test_{module}.py -v`
3. Verify all tests still PASS
4. Report: Refactoring done

**Repeat RED-GREEN-REFACTOR for each function until all features implemented.**

## Step 3: Final Security Review and Quality Standards

**Note**: Security should have been integrated throughout RED-GREEN-REFACTOR cycles. This step is final verification and gap filling.

1. **Verify CodeGuard compliance**:
   - Review relevant CodeGuard files identified in Step 1
   - Verify all security controls implemented (input validation, sanitization, etc.)
   - Verify all security test cases pass
   - Document which CodeGuard files were applied and why
   - **Fill any security gaps** discovered during review

2. **Verify code standards compliance**:
   - All modules have ABOUTME comments (2 lines at top)
   - All functions have Google-style docstrings
   - Type hints on all function signatures
   - Use pathlib.Path for file operations (platform independence)
   - Use project logger (not print statements)
   - No hardcoded credentials or secrets
   - No TODO comments without tracking issues

3. **Implement defensive coding**:
   - Validate inputs and handle invalid data gracefully
   - Provide fallback values for optional parameters
   - Raise specific exceptions with clear messages
   - Handle edge cases (empty lists, None values, boundary conditions)
   - Add logging for important operations
   - Don't leak sensitive data in error messages or logs

## Step 4: Verify Against Acceptance Criteria

1. **Run automated checks**:
   - `pytest -v` - All tests pass
   - `pytest --cov=src/{module} --cov-report=term` - Coverage ≥ 90%
   - `ruff check src/{module} test/test_{module}.py` - Linting passes
   - `ruff format src/{module} test/test_{module}.py` - Formatting applied

2. **Review acceptance criteria checklist** from the spec:
   - Go through each criterion systematically
   - Check that each functional requirement is implemented
   - Verify edge cases are handled
   - Confirm integration requirements are met
   - Validate security requirements are satisfied
   - Check documentation is complete

3. **Create verification report**:
   - List each acceptance criterion with status:
     - ✅ Met: Fully implemented and tested
     - ❌ Not Met: Missing or incomplete
     - ⚠️ Partially Met: Implemented but needs refinement
   - For any unmet criteria, note specific issues
   - Document what needs to be refined

## Step 5: Iterative Refinement

1. **If any criteria are not met**:
   - Update the implementation to address specific issues
   - Add missing tests
   - Re-run automated checks
   - Re-verify against acceptance criteria
   - Repeat until all criteria are met

2. **Refinement priorities**:
   - Fix failing tests first (blocking issues)
   - Address security concerns (critical)
   - Fix linting/formatting errors (quality)
   - Implement missing core functionality
   - Handle edge cases
   - Improve documentation
   - Optimize performance if requirements not met

3. **Quality gates** (must pass before completion):
   - ✅ All tests pass with pristine output
   - ✅ Test coverage ≥ 90%
   - ✅ Ruff checks pass (no errors)
   - ✅ All code documented
   - ✅ All acceptance criteria met
   - ✅ Security review passed
   - ✅ Platform independence verified

## Step 6: Final Validation and Documentation

1. **Run final checks**:
   - `pytest -v` passes with no errors
   - `pytest --cov=src --cov-report=html` shows ≥ 90% coverage
   - `ruff check src/ test/` passes
   - Module can be imported: `python -c "import src.{module}"`
   - All acceptance criteria verified

2. **Update documentation**:
   - Update docs/SPEC-CROSS-REFERENCE.md with source and test files
   - Update docs/INDEX.md if new modules added
   - Update specification with implementation status
   - If errors were self-fixed, update docs/rules/error-resolution-kb.md

3. **Create execution log** in docs/output-logs/{timestamp}-code-generation.md:
   - All TDD cycles completed (RED-GREEN-REFACTOR for each feature)
   - CodeGuard files applied and rationale
   - Test results at each stage
   - Coverage achieved
   - Issues encountered and resolutions
   - Files created/updated
   - Acceptance criteria verification results

4. **Provide implementation summary**:
   - ✅ Confirm implementation completed successfully
   - 📁 Location of source and test files
   - 🧪 Test results (count, coverage %)
   - 🔒 CodeGuard rules applied
   - ✅ List of key features implemented
   - 📋 Summary of acceptance criteria met
   - 🔗 Links to updated documentation
   - ⏭️ Next step: Human code review and approval

## Important Guidelines

- **Iterative approach**: Refine until all criteria met, don't stop after first pass
- **TDD discipline**: ALWAYS write tests BEFORE implementation code
- **Security-first development**: Integrate security at every TDD cycle, not as an afterthought
  - Write security tests in RED phase
  - Implement secure defaults in GREEN phase
  - Verify CodeGuard compliance in REFACTOR phase
  - Never skip security for "speed" - it's a critical requirement
  - always validate inputs and sanitize outputs
  - protect sensitive data
- **Type safety**: Use type hints throughout
- **Pattern consistency**: Follow existing code patterns in the project
- **Defensive coding**: Handle edge cases and invalid inputs gracefully
- **Performance**: Only optimize if spec requires it; don't over-optimize
- **Documentation**: Document as you code, not as an afterthought
- **Platform independence**: Use pathlib.Path, avoid platform-specific code
- **No placeholders**: Implement complete, production-ready code

## Error Handling

- If spec file missing, list available specs in docs/specifications/
- If tests fail, debug and fix iteratively (don't skip)
- If acceptance criteria unclear, implement based on best judgment and note assumptions
- If dependencies missing, add to requirements.txt
- If unsure about CodeGuard application, reference the specific guideline file
```

## Example Usage

### With Claude Code

```
Use the generate-code-from-spec prompt for docs/specifications/spec_auth.md
```

### With GitHub Copilot

```
@workspace Implement @docs/specifications/spec_auth.md using TDD following @.github/instructions/tdd-workflow.instructions.md. Apply relevant CodeGuard security rules and update the cross-reference table.
```

## Expected Output

- Source code: `src/{module}.py`
- Tests: `test/test_{module}.py`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Updated: `docs/INDEX.md`
- Log: `docs/output-logs/{timestamp}-code-generation.md`
- Updated (if errors): `docs/rules/error-resolution-kb.md`

## Example: TDD Cycle for Calculator Module

### Cycle 1: Add Function

**🔴 RED - Write Failing Test:**
```python
# test/test_calculator.py
import pytest
from src.calculator import add

def test_add_two_positive_numbers():
    """Test that add() correctly sums two positive numbers."""
    result = add(2, 3)
    assert result == 5
```

Run: `pytest test/test_calculator.py::test_add_two_positive_numbers -v`
Result: ❌ FAIL (ImportError: cannot import name 'add')

**🟢 GREEN - Write Minimal Code:**
```python
# src/calculator.py
# ABOUTME: Calculator module for basic arithmetic operations
# ABOUTME: Provides functions for addition, subtraction, multiplication, and division

def add(a, b):
    return a + b
```

Run: `pytest test/test_calculator.py::test_add_two_positive_numbers -v`
Result: ✅ PASS

**🔵 REFACTOR - Improve Code:**
```python
# src/calculator.py (after refactoring)
# ABOUTME: Calculator module for basic arithmetic operations
# ABOUTME: Provides functions for addition, subtraction, multiplication, and division

"""Calculator module for basic arithmetic operations."""

def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0.1, 0.2)
        0.3
    """
    return a + b
```

Run: `pytest test/test_calculator.py -v`
Result: ✅ PASS

### Cycle 2: Edge Case - Type Validation

**🔴 RED - Write Failing Test:**
```python
# test/test_calculator.py
def test_add_with_invalid_type():
    """Test that add() raises TypeError for invalid input."""
    with pytest.raises(TypeError):
        add("2", 3)
```

Run: `pytest test/test_calculator.py::test_add_with_invalid_type -v`
Result: ❌ FAIL (test expects TypeError but none raised)

**🟢 GREEN - Write Minimal Code:**
```python
def add(a: float, b: float) -> float:
    """[docstring same as before]"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
```

Run: `pytest test/test_calculator.py::test_add_with_invalid_type -v`
Result: ✅ PASS

**🔵 REFACTOR - Improve Code:**
```python
def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        Sum of a and b

    Raises:
        TypeError: If either argument is not a number

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0.1, 0.2)
        0.3
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers, got {type(a).__name__} and {type(b).__name__}")
    return a + b
```

Run: `pytest test/test_calculator.py -v`
Result: ✅ PASS (2/2 tests)

### Final Verification

```bash
# Run all tests
$ pytest test/test_calculator.py -v
======================== test session starts ========================
test/test_calculator.py::test_add_two_positive_numbers PASSED
test/test_calculator.py::test_add_with_invalid_type PASSED
======================== 2 passed in 0.05s =========================

# Check coverage
$ pytest --cov=src.calculator --cov-report=term test/test_calculator.py
---------- coverage: platform win32, python 3.14.0 -----------
Name                Cov
-----------------------------------
src/calculator.py   100%
-----------------------------------
TOTAL               100%

# Check linting
$ ruff check src/calculator.py test/test_calculator.py
All checks passed!

# Check formatting
$ ruff format src/calculator.py test/test_calculator.py
2 files left unchanged
```

**Implementation Summary:**
- ✅ 2 functions implemented (add function with validation)
- ✅ 2 tests passing
- ✅ 100% code coverage
- ✅ All linting checks passed
- ✅ Docstrings complete
- ✅ Type hints applied
- ✅ Edge cases handled
