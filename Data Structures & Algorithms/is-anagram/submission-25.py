class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs={}
        ht={}
        # {r:2,a:2,c:2,e:1}
        for i,n in enumerate(s):
            if not n in hs:
                hs[n]=1
            else:
                hs[n]+=1
        # {r:2,a:2,c:2,e:1}
        for i,n in enumerate(t):
            if not n in ht:
                ht[n]=1
            else:
                ht[n]+=1
        print(sorted(ht),sorted(hs))
        return ht==hs