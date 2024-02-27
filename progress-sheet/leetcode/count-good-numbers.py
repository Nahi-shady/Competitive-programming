class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def f(m):
            if m == 1:
                return 0

            return 2*f(m//2) + (m//2)%2

        return  (pow(4, f(n), 10**9 + 7) * pow(5, f(n+1), 10**9 + 7))% (10**9 + 7)
