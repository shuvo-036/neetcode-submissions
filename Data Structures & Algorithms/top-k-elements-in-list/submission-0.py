class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        bucket =[[] for _ in range(len(nums)+1)]
        for num , key in freq.items():
            bucket[key].append(num)   

        res =[]
        
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) ==k:
                    return res