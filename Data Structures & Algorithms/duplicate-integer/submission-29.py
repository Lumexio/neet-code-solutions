class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive solution
        hashD=dict()
        for n in nums:
            if n in hashD: return True
            else: hashD[n]=1
        return False

        