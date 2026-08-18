class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        res = ""
        counter = Counter(t)
        total = sum(counter.values())
    
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1

                if counter[s[r]] >= 0:
                    total -= 1
            
            while total == 0:
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        total += 1
                l += 1
        return res