class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs.sort(key = lambda x:len(x))
        res = ""
        shortest=min(strs,key=len)
        for i, letter in enumerate(shortest):
            for word in strs:
                if i>len(word)-1:return res
                if word[i] != letter:
                    return res
            res += letter
        return res