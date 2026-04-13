class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i,n in enumerate(nums):
            comp=target-n
            print(i,n)
            if comp in hashMap:
                return [hashMap[comp],i]
            else:
                hashMap[n]=i
        return [0,0]

