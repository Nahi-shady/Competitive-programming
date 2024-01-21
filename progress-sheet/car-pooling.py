class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(i[2] for i in trips)
        prefix = [0]*n
        for passenger, start, stop in trips:
            if passenger > capacity:
                return False
            prefix[start-1] += passenger
            prefix[stop-1] -= passenger
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            if prefix[i] > capacity:
                return False
        return True