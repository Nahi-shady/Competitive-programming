class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        ans = []
        for first, last, seats in bookings:
            print(first, last)
            prefix[first-1] += seats
            prefix[last] -= seats
        ans = [prefix[0]]
        for i in range(1, n):
            ans.append(ans[-1] + prefix[i])
        return ans