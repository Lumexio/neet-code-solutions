class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive for i,n in enumerate(nums):
        #     for j,m in enumerate(nums):
        #         if i==j: continue
        #         if n == m: return True
        # return False
        
        #optimized
        dat=set()
        for n in nums:
            if n in dat: return True
            else: dat.add(n)
        return False
