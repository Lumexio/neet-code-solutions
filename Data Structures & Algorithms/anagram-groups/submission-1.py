class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsHash=[]
        resp=[]
        for word in strs:
            current=''.join(sorted(word))
            if current not in strsHash:
                strsHash.append(current)
            

        for n in strsHash:
            currentGroup=list()
            for word in strs:
                current=''.join(sorted(word))
                if n == current:
                    currentGroup.append(word)
        
            resp.append(currentGroup)
        
        return resp

        
