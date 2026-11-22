import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        res = heapq.nlargest(k, d.items(), key = lambda x:x[1])
        return [x[0] for x in res]