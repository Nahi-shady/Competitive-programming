class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = 0
        score = 0
        for i in range(len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    score += 2**(stack-1)
                stack -= 1
            else:
                stack += 1
            
        return score