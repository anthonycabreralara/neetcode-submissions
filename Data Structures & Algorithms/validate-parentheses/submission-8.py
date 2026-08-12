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
                # It's an opening parenthesis, push it onto the stack
                stack.append(char)
            elif char in matching_parentheses:
                # It's a closing parenthesis, check if it matches the last opened one
                if stack and stack[-1] == matching_parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Invalid character, return False
                return False
        
        # If the stack is empty, all parentheses were matched
        return len(stack) == 0
