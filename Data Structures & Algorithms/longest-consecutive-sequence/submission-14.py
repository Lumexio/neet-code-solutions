class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1: return len(nums)

        res=0

        dataSet=set(nums)

        print(dataSet)
        for n in nums:
            curr=n
            acc=0
            while curr in dataSet:
                acc+=1
                curr+=1
                if acc>=res:
                    res=acc


        return res



