class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for s in strs:
            a = [0] * 26
            for i in s:
                a[ord(i)-ord('a')] += 1
            a = tuple(a)
            d[a] = d.get(a, []) + [s]
        for k, v in d.items():
            res.append(v)
        return res