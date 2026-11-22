class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m>n:
            return False
        left, right = 0, 0
        d1 = {}
        for i in range(m):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
        
        d2 = {}
        while right<m:
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            right += 1
        if len(d1) == len(d2) and d1==d2:
            return True
        
        while right<n:
            d2[s2[left]] -= 1
            if d2[s2[left]]==0:
                del d2[s2[left]]
            left += 1
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            right += 1
            if len(d1) == len(d2) and d1==d2:
                return True
        return False