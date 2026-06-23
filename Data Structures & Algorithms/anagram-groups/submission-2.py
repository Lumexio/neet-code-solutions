class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashData=[]
        resp=[]
        for n in strs:
            curr=''.join(sorted(n))
            if curr not in hashData:
                hashData.append(curr)
        for n in hashData:
            currGroup=list()
            for m in strs:
                curr=''.join(sorted(m))
                if n == curr:
                    currGroup.append(m)
            resp.append(currGroup)
        return resp