class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        i=0
        while(True):
            if i>=len(strs[0]): return pref
            curr=strs[0][i]
            for word in strs:
                if i >= len(word): return pref
                if curr!=word[i]: return pref
            pref+=curr
            i+=1
        return pref

