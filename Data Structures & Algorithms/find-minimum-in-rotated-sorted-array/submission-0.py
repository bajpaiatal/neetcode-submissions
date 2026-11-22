class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if nums[0]<=nums[n-1]:
            return nums[0]
        if nums[n-1]<=nums[0] and nums[n-1]<=nums[n-2]:
            return nums[n-1]
        low = 1
        high = n-2
        while low<=high:
            mid = low + (high-low)//2
            print(low, mid, high)
            if nums[mid]<=nums[mid-1] and nums[mid]<=nums[mid+1]:
                return nums[mid]
            elif nums[mid]>=nums[low] and nums[mid]>=nums[high]:
                low = mid+1
            else:
                high = mid-1
        return -1