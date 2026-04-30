class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1: return len(nums)
        dataSet=set(nums)
        res=0
        for n in nums:
            curr=n
            acc=0
            while curr in dataSet:
                acc+=1
                curr+= 1
                if acc>=res:
                    res=acc
                print(curr,acc)
 
            
            
            
      
       
       
        return res