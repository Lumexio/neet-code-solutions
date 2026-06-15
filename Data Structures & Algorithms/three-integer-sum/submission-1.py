class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        target=0
        resp=list()
        nums.sort() # n^2

        print(nums)
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            else:
                left,right=i+1,len(nums)-1
                while(left<right):
                    b,c=nums[left],nums[right]
                    sumCurr=a+b+c    
                    if sumCurr>target:
                        right-=1
                    elif sumCurr<target:
                        left+=1
                    else:
                        resp.append([a,b,c])
                        left+=1
                        while nums[left]==nums[left-1] and left<right:
                            left+=1
        print(resp)
        return resp

         