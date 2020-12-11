'''
    24ms, faster than 94.4% of python sols
    14.4MB, less than 12.3% of python sols
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) > 0:
                if stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '(' and char == ")":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return len(stack) == 0
