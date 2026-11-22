class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res = res + f"{len(st)}#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            l, s = s.split('#', 1)
            l = int(l)
            res.append(s[:l])
            s = s[l:]
        return res