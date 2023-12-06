class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i = 1
        count = 0
        while i < len(points):
            diff0 = points[i][0] - points[i-1][0]
            diff1 = points[i][1] - points[i-1][1]
           
            count += max(abs(diff0), abs(diff1))
            i+=1
          
        return count
