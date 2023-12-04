class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        ma = max(candies)
        for i in candies:
            if i + extraCandies >= ma:
                res.append(True)
            else:
                res.append(False)
        return res