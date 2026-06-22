from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sortS=defaultdict(int)
        # sortT=defaultdict(int)

        # for char in s:
        #     sortS[char]+=1
        # for char in t:
        #     sortT[char]+=1

        # if sortT == sortS:
        #     return True
        # else:
        #     return False
        return Counter(s) == Counter(t)