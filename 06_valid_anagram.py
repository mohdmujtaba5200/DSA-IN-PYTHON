def is_anagram(s: str, t: str) -> bool:
    """
    Determines if string t is an anagram of string s.
    Uses frequency mapping for O(N) time complexity.
    """
    # Anagrams must have identical length
    if len(s) != len(t):
        return False

    # Track character counts for both strings
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    # Compare character frequency dictionaries
    return count_s == count_t

# Test execution
if __name__ == "__main__":
    str1, str2 = "anagram", "nagaram"
    print(f"Are '{str1}' and '{str2}' anagrams? -> {is_anagram(str1, str2)}")