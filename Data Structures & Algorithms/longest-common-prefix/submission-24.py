class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comPre=""
        i=0
        while(True):
            if i>len(strs[0])-1: return comPre
            currL=strs[0][i]
            for n in strs:
                if len(n)<1: return ""
                if i>=len(n): return comPre
                if currL!=n[i]: return comPre
                
            comPre+=currL
            i+=1
        return comPre