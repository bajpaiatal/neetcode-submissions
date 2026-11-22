class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(t), len(s)
        if m>n:
            return ""
        freq = [0]*128
        start = 0
        minLength = float('inf')
        for i in range(m):
            freq[ord(t[i])] += 1
        missing = m
        left, right = 0, 0
        while right<n:
            idx = ord(s[right])
            if freq[idx] > 0:
                missing -= 1
            freq[idx] -= 1

            while missing==0 and left<=right:
                if (right-left+1)<minLength:
                    start = left
                    minLength = right-left+1
                idx = ord(s[left])
                freq[idx] += 1
                if freq[idx] > 0:
                    missing += 1
                left += 1
            right += 1
            # print(left, right, missing)
        
        if minLength == float('inf'):
            return ""
        return s[start:start+minLength]          