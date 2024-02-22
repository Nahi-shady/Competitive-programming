class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        next_g = [0] * len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                popp = stack.pop()
                next_g[popp] = i - popp

            stack.append(i)

        return next_g