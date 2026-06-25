class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashData=defaultdict(int)

        for n in nums:
            hashData[n]+=1

            
        
        temp={key: value for key, value in sorted(hashData.items(), key=lambda item: item[1],reverse=True)}
        print(temp)
        return list(temp)[0:k]