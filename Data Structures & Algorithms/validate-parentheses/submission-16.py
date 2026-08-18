class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {']': '[', '}': '{', ')': '('}
        for c in s:
            if c in paren and not stack:
                return False
            elif c in paren:
                prev = stack.pop()
                if paren[c] != prev:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0