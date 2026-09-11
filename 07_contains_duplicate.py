"""
LeetCode 217: Contains Duplicate
Topic: Arrays & Hashing
Strategy: Hash Set
Time Complexity: O(N)
Space Complexity: O(N)
"""

def contains_duplicate(nums: list[int]) -> bool:
    # Hash Set provides O(1) average lookup time
    seen = set()
    
    for num in nums:
        # If the number is already in our set, we found a duplicate
        if num in seen:
            return True
        seen.add(num)
        
    # If loop finishes, all elements are unique
    return False


if __name__ == "__main__":
    # Test Cases
    test1 = [1, 2, 3, 1]
    test2 = [1, 2, 3, 4]
    
    print(f"Test 1 [1, 2, 3, 1]: {contains_duplicate(test1)}")  # Expected: True
    print(f"Test 2 [1, 2, 3, 4]: {contains_duplicate(test2)}")  # Expected: False