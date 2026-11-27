class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for w in strs:
            curr="".join(sorted(w))
            if curr not in res: res[curr]=[]
            res[curr].append(w)
        return list(res.values())