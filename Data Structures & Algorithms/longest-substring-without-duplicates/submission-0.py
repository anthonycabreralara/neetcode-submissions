class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = set()
        max_length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in history:
                history.remove(s[l])
                l = l + 1
            
            history.add(s[r])
            max_length = max(r - l + 1, max_length)

        return max_length