class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sdat=dict()
        for i,n in enumerate(nums):
            c=target-n
            if c in sdat: return[sdat[c],i]
            else: sdat[n]=i
        return []