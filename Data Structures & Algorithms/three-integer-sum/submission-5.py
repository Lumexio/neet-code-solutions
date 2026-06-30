class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resp= list()
        target=0
        nums.sort()
        print(nums)
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                b,c=nums[l],nums[r]
                currSum=a+b+c
                if currSum>target:
                    r-=1
                elif currSum<target:
                    l+=1
                else:
                    resp.append([a,b,c])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return resp