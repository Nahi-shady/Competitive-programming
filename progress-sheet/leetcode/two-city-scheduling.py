class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda costs: costs[0]-costs[1])
        a = 0
        b = 0
        n = len(costs)
        for i in range(n):
            if i < n//2:
                a += costs[i][0]
            else:
                a += costs[i][1]
        return a + b