class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x,y):
            return (x**2 + y**2) ** 0.5

        points.sort(key = lambda i : distance(i[0], i[1]))

        return points[:k]