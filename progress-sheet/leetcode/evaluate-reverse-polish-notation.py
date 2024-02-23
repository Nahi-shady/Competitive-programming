class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-','*', '/'}
        for i in tokens:
            if i in ops:
                op1 = stack.pop()
                op2 = stack.pop()
                if i == '+':
                    res = op1 + op2
                elif i == '-':
                    res = op2 - op1
                elif i == '*':
                    res = op1 * op2
                else:
                    res = int(op2 / op1)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[-1]