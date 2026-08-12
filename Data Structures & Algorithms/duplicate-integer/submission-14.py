class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        libSet=set()

        for i in nums:
            if i in libSet: return True
            libSet.add(i)
        return False