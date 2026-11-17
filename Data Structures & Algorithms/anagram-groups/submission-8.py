class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for n in strs:
            curr=''.join(sorted(n))
            r[curr].append(n)
        return list(r.values())