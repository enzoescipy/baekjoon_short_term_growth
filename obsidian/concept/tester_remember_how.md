# Simple Tester Class Guide

## Basic Structure
```python
class Tester:
    def __init__(self):
        self.test_cases = []
        self.results = {"passed": 0, "failed": 0, "total": 0}
    
    def add_test(self, items, weight_limit, expected_output):
        """Add test case"""
        self.test_cases.append({
            "items": items,
            "limit": weight_limit,
            "expected": expected_output
        })
    
    def run_all(self, solution_function):
        """Run all tests"""
        # Run tests and print results
        # Return True if all passed, False otherwise
```

## Quick Usage

1. Create tester:
   ```python
   tester = Tester()
   ```

2. Add test cases:
   ```python
   # Simple example
   tester.add_test([(6, 13), (4, 8), (3, 6)], 7, 14)
   
   # Format: add_test(items, weight_limit, expected_result)
   # items: list of (weight, value) tuples
   ```

3. Add default tests (optional):
   ```python
   tester.add_default_tests()  # Adds several standard test cases
   ```

4. Run the tests:
   ```python
   all_passed = tester.run_all(your_solution_function)
   ```

## Sample Output
```
===== RUNNING TESTS =====
Test #1: PASSED ✓ (Got: 14, Expected: 14)
Test #2: FAILED ✗ (Got: 0, Expected: 146)

===== SUMMARY =====
Passed: 1/2 tests
```

## Advanced: Comparison-Based Testing
```python
def compare_all(self, optimized_solution, brute_force_solution):
    """Compare optimized solution with brute force solution"""
    for i, test in enumerate(self.test_cases):
        opt_result = optimized_solution(test["items"], test["limit"])
        brute_result = brute_force_solution(test["items"], test["limit"])
        
        if opt_result == brute_result:
            print(f"Test #{i+1}: PASSED ✓ (Got: {opt_result})")
            self.results["passed"] += 1
        else:
            print(f"Test #{i+1}: FAILED ✗ (Got: {opt_result}, Expected: {brute_result})")
            self.results["failed"] += 1
        self.results["total"] += 1
```

### Usage Example
```python
# Create tester and add test cases
tester = Tester()
tester.add_test([(6, 13), (4, 8), (3, 6)], 7, 14)

# Run comparison test
tester.compare_all(optimized_solution, brute_force_solution)
```

## Remember
- Test cases are triples: (items, weight_limit, expected_output)
- Items are (weight, value) tuples
- Use meaningful test cases including edge cases (empty, too heavy, etc.)
- The solution function must take exactly two parameters: items and weight_limit 