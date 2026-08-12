class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses_pair = { "(": ")", "{": "}", "[": "]" }
        stack = []

        for char in s:
            if char in parentheses_pair:
                stack.append(char)
            elif len(stack) > 0 and char == parentheses_pair.get(stack[len(stack) - 1]):
                stack.pop()
            else:
                return False

        
        if len(stack) > 0:
            return False

        return True