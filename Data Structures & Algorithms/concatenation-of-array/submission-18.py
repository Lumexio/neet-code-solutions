class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(n*2)
        for i,nums in enumerate(nums):
            ans[i]=nums
            ans[n+i]=nums
        return ans