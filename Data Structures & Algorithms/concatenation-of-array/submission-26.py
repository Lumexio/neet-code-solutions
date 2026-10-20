class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(2*n)
        for i,m in enumerate(nums):
            ans[i]=m
            ans[i+n]=m
        return ans