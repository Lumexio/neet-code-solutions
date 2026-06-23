class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict=list()
        resp=list()

        for n in strs:
            curr=''.join(sorted(n))
            if curr not in hashDict:
                hashDict.append(curr)
        
        for n in hashDict:
            groupCurr=list()
            for word in strs:
                curr=''.join(sorted(word))
                if n == curr:
                    groupCurr.append(word)
            resp.append(groupCurr)
        return resp