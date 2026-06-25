class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashData=defaultdict(int)

        for n in nums:
            hashData[n]+=1

            
        
        temp=sorted(hashData,key=hashData.get,reverse=True)
        return temp[:k]