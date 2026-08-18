"""
k = 1 - 1 = 0
AAABABB
l
    r
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        distinct = set(s)
        res = 0
        for c in distinct:
            l = 0
            kc = k
            for r in range(len(s)):
                if s[r] != c:
                    kc -= 1
                
                while kc < 0:
                    if s[l] != c:
                        kc += 1
                    l += 1
                res = max(res, r - l + 1)
        
        return res