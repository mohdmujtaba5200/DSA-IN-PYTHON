"""
Rotated Sorted Array Search & Minimum Detection
-----------------------------------------------
Implementation of Binary Search to locate the minimum element (pivot point)
in a rotated sorted array without duplicates in O(log N) runtime.

Author: Mohd Mujtaba 
Module: Data Structures & Algorithms Core
"""

from typing import List, Optional


def find_minimum_rotated(nums: List[int]) -> Optional[int]:
    """
    Finds the minimum element in a rotated sorted array using iterative Binary Search.

    Parameters:
        nums (List[int]): A list of integers sorted in ascending order, 
                          then rotated at an unknown pivot index.

    Returns:
        Optional[int]: The minimum integer value in the array, or None if input is empty.

    Complexity Analysis:
        - Time Complexity: O(log N)
            The search space is halved at every iteration (N -> N/2 -> N/4 ... -> 1).
            Recurrence relation: T(N) = T(N/2) + O(1), solved via Master Theorem to O(log N).
        - Space Complexity: O(1)
            Iterative implementation maintains only two pointer variables (low, high),
            requiring constant additional memory allocation on the stack.
    """
    if not nums:
        return None

    low: int = 0
    high: int = len(nums) - 1

    # Array is not rotated or has a single element
    if nums[low] <= nums[high]:
        return nums[low]

    while low < high:
        mid: int = low + (high - low) // 2  # Prevents potential integer overflow

        # If mid element is strictly greater than high element,
        # the rotation pivot MUST lie in the right subarray.
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            # Pivot lies at mid or in the left subarray.
            high = mid

    return nums[low]


def run_unit_tests() -> None:
    """Automated verification suite covering standard, edge, and boundary cases."""
    test_cases = [
        {"name": "Standard Rotated Array", "input": [4, 5, 6, 7, 0, 1, 2], "expected": 0},
        {"name": "Unrotated Sorted Array", "input": [1, 2, 3, 4, 5], "expected": 1},
        {"name": "Single Element Array", "input": [10], "expected": 10},
        {"name": "Two Elements Rotated", "input": [2, 1], "expected": 1},
        {"name": "Two Elements Sorted", "input": [1, 2], "expected": 1},
        {"name": "Empty Input Handling", "input": [], "expected": None},
        {"name": "Pivot at Last Element", "input": [2, 3, 4, 5, 1], "expected": 1},
    ]

    print("Running Verification Test Suite...\n" + "-" * 40)
    passed = 0
    for test in test_cases:
        result = find_minimum_rotated(test["input"])
        assert result == test["expected"], f"FAILED: {test['name']} - Got {result}, expected {test['expected']}"
        print(f"[PASS] {test['name']}: Input={test['input']} | Output={result}")
        passed += 1

    print("-" * 40)
    print(f"Test Suite Execution Complete: {passed}/{len(test_cases)} Passed Successfully.\n")


if __name__ == "__main__":
    run_unit_tests()