def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds two numbers in the array that add up to the target.
    Uses a Hash Map for O(N) time complexity.
    """
    # Hash map to store numbers and their indices: {number: index}
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        # If the required value exists in our map, return both indices
        if complement in seen:
            return [seen[complement], index]

        # Otherwise, record current number and its index
        seen[num] = index

    return []

# Test execution
if __name__ == "__main__":
    test_nums = [2, 7, 11, 15]
    test_target = 9
    print(f"Two Sum Result for target {test_target}: {two_sum(test_nums, test_target)}")