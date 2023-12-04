class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        l =  min(start, destination)
        r = max(start, destination)
        
        return min(sum(distance[l:r]), sum(distance[r:]+distance[:l]))