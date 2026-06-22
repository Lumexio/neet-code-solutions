class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS=sorted(s)
        sortT=sorted(t)

        if sortT == sortS:
            return True
        else:
            return False