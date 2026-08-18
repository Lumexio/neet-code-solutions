class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r=c=0
        for n in nums:
            if n==1:
                c+=1
            else:c=0 
            if c>r:
                r=c
        return r