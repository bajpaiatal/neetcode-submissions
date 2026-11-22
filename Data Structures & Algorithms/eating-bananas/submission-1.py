import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n>h:
            return -1
        low = 1
        high = max(piles)
        while low<=high:
            mid = low + (high-low)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours>h:
                low = mid+1
            else:
                high = mid-1
        return low