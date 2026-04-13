class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)): return False
       
        ShashMap={}
        ThashMap={}
        for n in set(list(s)):
            ShashMap[n]=0
        for n in set(list(t)):
            ThashMap[n]=0
        
        for n in list(s):
            
            if n in ShashMap: 
               
                ShashMap[n]+=1
        
        for n in list(t):
            if n in ThashMap: ThashMap[n]+=1
       
        for n in ShashMap:
            if n not in ThashMap or ShashMap[n] != ThashMap[n]: return False
            elif n in ThashMap and ShashMap[n] == ThashMap[n]: continue

        return True

    