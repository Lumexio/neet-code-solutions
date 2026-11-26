class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)  # Runs in C, O(N) time
        for i, letter in enumerate(shortest):
            for word in strs:
                if word[i] != letter:
                    return shortest[:i]  # Slicing once is faster than res += letter
        return shortest