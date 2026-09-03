class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive 1  O(n^2)
        # for i,n in enumerate(nums):
        #     for j,m in enumerate(nums):
        #         if j == i: continue
        #         if n==m: return True
        # return False
        # naive 2    O(nlogn)
        # nums.sort()
        # print(nums)
        # for i in range(len(nums)):
        #     if nums[i-1]==nums[i]:
        #         return True
        # return False
        dat_h=dict()
        for n in nums:
            if n in dat_h:
                return True
            dat_h[n]=n
        return False