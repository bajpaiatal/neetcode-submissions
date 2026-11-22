import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        li = []
        for i in range(min(k, n)):
            li.append((-1*nums[i], i))
        heapq.heapify(li)
        res = []
        # print(li)
        
        for i in range(k, n):
            res.append(-1*li[0][0])
            while li and li[0][1] <= i-k:
                heapq.heappop(li)
            heapq.heappush(li, (-1*nums[i], i))
        res.append(-1*li[0][0])
        return res