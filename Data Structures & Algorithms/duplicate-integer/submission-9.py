class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<2: return False
        hashMap={}
        for n in nums:
            if n in hashMap:
                hashMap[n]+=1
                if hashMap[n] %2 ==0: return True
            hashMap[n]=1

        print(hashMap)
        return False