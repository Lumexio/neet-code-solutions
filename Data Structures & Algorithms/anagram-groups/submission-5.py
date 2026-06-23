class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict=defaultdict(list)


        for n in strs:
            curr=''.join(sorted(n))
            hashDict[curr].append(n)
        
        return list(hashDict.values())