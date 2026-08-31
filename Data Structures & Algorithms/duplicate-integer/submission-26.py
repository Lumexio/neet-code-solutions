class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)
        # datD=set()
        # for n in nums:
        #     if n in datD:return True 
        #     else:datD.add(n)        
        # return False

        # for i,n in enumerate(nums):
        #     for j,m in enumerate(nums):
        #         if i ==j : continue
        #         if n == m: return True
        # return False
        