class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sS="".join(sorted(s))
        tS="".join(sorted(t))
        return sS==tS