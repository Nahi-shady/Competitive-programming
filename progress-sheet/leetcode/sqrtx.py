class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l + 1 < r:
            mid = (l+r) // 2
            if mid*mid > x:
                r = mid
            elif mid*mid == x:
                return mid
            else:
                l = mid
        return l if x else 0