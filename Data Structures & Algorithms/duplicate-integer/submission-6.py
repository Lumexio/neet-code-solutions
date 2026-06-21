class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<2: return False
        hashMap={}
        for n in nums:
            if n in hashMap: return True
            hashMap[n]=1

  
        return False