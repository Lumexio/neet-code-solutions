class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k,r=0,0

        while(r<len(nums)):
            if nums[r]!=val:
                nums[k]=nums[r]
                k+=1
            r+=1
        return k