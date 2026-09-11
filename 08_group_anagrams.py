"""
LeetCode 49: Group Anagrams
Topic: Arrays & Hashing
Strategy: Sorting Key with Hash Map
Time Complexity: O(N * K log K)  [N = number of words, K = max word length]
Space Complexity: O(N * K)
"""

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    # Initialize a hash map where default values are empty lists
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Sort the characters of the word to create a normalized key
        # e.g., "eat" -> ['a', 'e', 't'] -> "aet"
        sorted_key = "".join(sorted(word))
        
        # Group original words under the sorted key
        anagram_map[sorted_key].append(word)
        
    # Return all grouped lists from the dictionary
    return list(anagram_map.values())


if __name__ == "__main__":
    # Test Case
    sample_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = group_anagrams(sample_words)
    
    print("Grouped Anagrams Result:")
    print(output)
    # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]