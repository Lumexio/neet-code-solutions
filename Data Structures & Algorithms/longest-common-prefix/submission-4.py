class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        i=0
        while(True):
            if not strs or i>=len(strs[0]):
                return pref
            curr_char=strs[0][i]
            for word in strs:
                if not word: return pref
                if len(pref)>=len(word): return pref
                if len(word)>=i and curr_char!=word[i]:
                    return pref
            pref+=curr_char
            i+=1
        return pref