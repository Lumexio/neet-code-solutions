class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdata={}

        for i,n in enumerate(nums):
            comp=target-n
            if comp in hashdata:
                return [hashdata[comp],i]
            else:
                hashdata[n]=i
        return [0,0]