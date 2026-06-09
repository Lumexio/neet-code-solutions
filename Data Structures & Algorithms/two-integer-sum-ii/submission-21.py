class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while(left<right):
            curr=numbers[left]+numbers[right]
            if target ==curr:
                return [left+1,right+1]
            if target<curr:
                right-=1
            else:
                left+=1
        return [0,0]
