class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        d = {}
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] in d and d[s[i]]>start:
                start = d[s[i]]
            d[s[i]] = i
            res = max(res, i-start)
        return res
