class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0
        visited = set()
        for r in range(n):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            res = max(res, len(visited))
        return res