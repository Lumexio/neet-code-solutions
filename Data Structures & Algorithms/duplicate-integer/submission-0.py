class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet=set(nums)
        hashMap={}
        for num in hashSet:
            hashMap[num]=0
       
        for num in nums:
            hashMap[num]+=1
            if(hashMap[num]>1): 
                return True 

        return False
       
        