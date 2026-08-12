class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s.replace(" ", "")
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha() and not s[left].isnumeric():
                left = left + 1
                continue
            if not s[right].isalpha() and not s[right].isnumeric():
                right = right - 1
                continue
            print(s[left] + " " + s[right])
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True
        