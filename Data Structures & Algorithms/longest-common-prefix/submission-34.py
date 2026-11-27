class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i,letter in enumerate(strs[0]):
            for w in strs:
                if i == len(w) or letter!=w[i]:
                    return res
            res+=letter
        return res
