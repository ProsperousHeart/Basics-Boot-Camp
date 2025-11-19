# Test Case Generation Instructions

**Last Updated**: 2025-11-09

Guidelines for writing comprehensive test cases following TDD principles.

## 🎯 Test Categories

### Unit Tests

Test individual functions/methods in isolation

### Integration Tests

Test component interactions

### End-to-End Tests

Test complete user workflows

## 📋 Test Case Template

```python
def test_{feature}_{scenario}_{expected_result}():
    """
    Test that {feature} {scenario} results in {expected result}.

    References:
        - Specification: docs/specifications/spec_xxx.md
        - CodeGuard: .github/instructions/codeguard-*.instructions.md (if applicable)
    """
    # Arrange
    # Setup test data and conditions

    # Act
    # Execute the code being tested

    # Assert
    # Verify expected results
```

**TODO**: Expand with comprehensive test case examples and patterns

## 🔒 Security Test Cases

Reference relevant CodeGuard files when writing security tests.

**TODO**: Add security test case examples

## 📚 Related Documentation

- [TDD Workflow](tdd-workflow.instructions.md)
- [Master Workflow](master-workflow.md)
