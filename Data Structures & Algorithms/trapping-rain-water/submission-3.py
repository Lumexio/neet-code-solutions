class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        maxL,maxR=height[l],height[r]
        while l<r:
            if maxL<=maxR:
                l+=1
                curr=maxL-height[l]
                if curr>=0:
                    res+=curr
                maxL=max(maxL,height[l])
            else:
                r-=1
                curr=maxR-height[r]
                if curr>=0:
                    res+=curr
                maxR=max(maxR,height[r])
        return res