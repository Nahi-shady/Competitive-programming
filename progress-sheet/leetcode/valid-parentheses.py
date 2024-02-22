class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(',
                ']': '[',
                '}': '{'
                }
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
        return False if stack else True