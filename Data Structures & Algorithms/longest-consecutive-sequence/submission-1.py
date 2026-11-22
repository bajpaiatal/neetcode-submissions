class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in st:
            if num-1 not in st:
                k = num+1
                while k in st:
                    k += 1
                res = max(res, k-num)
        return res