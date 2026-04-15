from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}

        for n in nums:
            if n not in hashMap:
                hashMap[n]=1
            elif n in hashMap:
                hashMap[n]+=1
        sorted_dict=dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        resp=[]
        acc=1
        for key,val in sorted_dict.items():
            resp.append(key)
            if acc == k:
                break
            acc+=1
        return resp