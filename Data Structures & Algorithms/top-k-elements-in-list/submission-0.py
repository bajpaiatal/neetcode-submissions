class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)

        res = [x[0] for x in sorted_d[:k]]
        return res