class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_arr = []
        suff_arr = []
        pre = 1
        suff = 1
        i = 0
        n = len(nums)
        while i<n:
            pre_arr.append(pre)
            suff_arr.append(suff)
            pre *= nums[i]
            suff *= nums[n-1-i]
            i += 1
        suff_arr = suff_arr[::-1]
        res = []
        i = 0
        while i<n:
            res.append(pre_arr[i]*suff_arr[i])
            i += 1
        return res
