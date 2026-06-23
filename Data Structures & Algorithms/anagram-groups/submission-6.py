class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            c="".join(sorted(s))
            res[c].append(s)
        return list(res.values())