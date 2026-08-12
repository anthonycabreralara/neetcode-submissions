class Solution:
    def isValid(self, s: str) -> bool:
        # If the length of s is odd, it can't be valid
        if len(s) % 2 != 0:
            return False
        
        # Dictionary for matching parentheses
        matching_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            print(f"Current stack: {stack}")
            print(f"Processing: {char}")
            
            if char in matching_parentheses.values():
                stack.append(char)
            elif char in matching_parentheses:
                if len(stack) > 0 and stack[-1] == matching_parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0
