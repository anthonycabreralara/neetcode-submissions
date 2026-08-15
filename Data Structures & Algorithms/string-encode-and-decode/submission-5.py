class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "-" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        curr = ""
        res = []
        l = 0
        while l < len(s):
            length = ""
            while s[l] != '-':
                length += s[l]
                l += 1
            length = int(length)
            l += 1
            for i in range(l, l+length):
                curr += s[i]
            res.append(curr)
            curr = ""
            l += length
        return res
            