class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m+n+1)//2
        low = max(0, k-n)
        high = min(m, k)
        while low<=high:
            mid1 = low + (high-low)//2
            mid2 = k-mid1
            l1 = nums1[mid1-1] if mid1>0 else float('-inf')
            l2 = nums2[mid2-1] if mid2>0 else float('-inf')
            r1 = nums1[mid1] if mid1<m else float('inf')
            r2 = nums2[mid2] if mid2<n else float('inf')
            if l1<=r2 and l2<=r1:
                if (m+n)%2==1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2))/2
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return -1