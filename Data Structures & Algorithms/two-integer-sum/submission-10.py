class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashD=dict()
        for i,n in enumerate(nums):
            c=target-n
            print(c,n)
            if c in hashD: return [hashD[c],i]
            else: hashD[n]=i
        return [0,0]