class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_d=dict()
        for n in nums:
            if n in hash_d:
                hash_d[n]+=1
            else: hash_d[n]=1
        

        for key,n in hash_d.items():
            if n>1: return key