class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i<n:
            if i!=0 and nums[i]==nums[i-1]:
                i += 1
                continue
            l = i+1
            h = n-1
            while l<h:
                val = nums[i] + nums[l] + nums[h]
                if val == 0:
                    res.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1
                elif val>0:
                    h -= 1
                else:
                    l += 1
                while l<h and l!=i+1 and nums[l]==nums[l-1]:
                    l += 1
                    continue
                while l<h and h!=n-1 and nums[h]==nums[h+1]:
                    h -= 1
                    continue
            i += 1
        return res
