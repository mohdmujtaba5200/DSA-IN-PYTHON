def binary_search(arr, target):
    """
    Returns the index of target in a sorted list 'arr' using Binary Search.
    Returns -1 if target is not present.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# --- Test Cases ---
if __name__ == "__main__":
    test_arr = [2, 3, 4, 10, 40]
    print(f"Index of 10: {binary_search(test_arr, 10)}")  # Expected: 3
    print(f"Index of 50: {binary_search(test_arr, 50)}")  # Expected: -1
    print(f"Index of 5 in [5]: {binary_search([5], 5)}")  # Expected: 0
    print(f"Index in empty array: {binary_search([], 10)}")  # Expected: -1