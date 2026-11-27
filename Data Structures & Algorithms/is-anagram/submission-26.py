class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sS=sorted(s)
        sT=sorted(t)
        return sS==sT
        