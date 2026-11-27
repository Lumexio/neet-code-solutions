class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for w in strs:
            curr="".join(sorted(w))
            res[curr].append(w)
        return list(res.values())