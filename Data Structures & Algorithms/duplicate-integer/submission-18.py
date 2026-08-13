class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        datD=set()

        for n in nums:
            if n in datD: return True
            datD.add(n)        
        return False
        # for i,n in enumerate(nums):
        #     for j,m in enumerate(nums):
        #         if i ==j : continue
        #         if n == m: return True
        # return False
        