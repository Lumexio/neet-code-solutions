class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hasD=dict()
        maxCurr=nums[0]
        for n in nums:
            
            if n not in hasD: hasD[n]=1
            else:
                hasD[n]+=1
                if hasD[maxCurr]<=hasD[n]: maxCurr=n
        return maxCurr