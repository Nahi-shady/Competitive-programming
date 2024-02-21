class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = i = 0
        end = points[0][1]
        while i < len(points):
            if end < points[i][0]:
                ans += 1
                end = points[i][1]
            i += 1
        return ans+1