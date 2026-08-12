class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower()

        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left = left + 1
                continue

            if not s[right].isalpha() and not s[right].isdigit():
                right = right - 1
                continue

            print("left: " + s[left] + ", right: " + s[right])

            if s[left] != s[right]:
                return False

            left = left + 1
            right = right - 1
        
        return True
        