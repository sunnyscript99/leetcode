class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(N + M) Time Complexity
        # O(1) Space Complexity (hashmap keys are bound to 26 chars)
        if len(s) != len(t):
            return False 
        char_counts = {}
        for c in s:
            char_counts[c] = char_counts.get(c, 0) + 1
        for c in t:
            if c not in char_counts or char_counts[c] == 0:
                return False
            char_counts[c] -= 1
        return True
