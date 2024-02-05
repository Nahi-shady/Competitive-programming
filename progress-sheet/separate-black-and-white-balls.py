class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
            elif i == '0':
                count += ones
        return count