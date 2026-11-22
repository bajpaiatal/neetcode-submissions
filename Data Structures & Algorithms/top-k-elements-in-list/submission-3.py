import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        heap = []
        for i,j in d.items():
            heapq.heappush(heap, (j, i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [y for x,y in heap]
        return res