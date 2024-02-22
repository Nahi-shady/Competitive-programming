class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if '..' in log and stack:
                stack.pop()
            elif '.' not in log:
                stack.append(log)
        return len(stack)