class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs.sort(key = lambda x:len(x))
        res = ""
        for i, letter in enumerate(strs[0]):
            for word in strs:
                if i>len(word)-1: return res
                if word[i] != letter:
                    return res
            res += letter
        return res