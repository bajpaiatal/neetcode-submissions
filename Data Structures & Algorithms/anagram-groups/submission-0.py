class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for s in strs:
            ns = ''.join(sorted(s))
            d[ns] = d.get(ns, []) + [s]
        for k, v in d.items():
            res.append(v)
        return res
