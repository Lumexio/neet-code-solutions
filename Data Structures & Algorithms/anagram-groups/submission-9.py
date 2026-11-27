class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for w in strs:
            cur="".join(sorted(w))
            res[cur].append(w)
        return list(res.values())
