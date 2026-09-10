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

        " So to prevent the usage of memory using hashmap i can have two temporal variables, curr count and max count, the idea is to rest the curr count every time y encounter a diferent element."
  
