class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        i=0
        while(True):
            if not strs: return pref
            if i>=len(strs[0]): return pref
            curr_char=strs[0][i]
            for word in strs:
                if not word : return pref
                if i>=len(word):return pref
                if word[i]!=curr_char:
                    return pref
            pref+=curr_char
            i+=1
        return pref
                