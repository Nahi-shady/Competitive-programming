class Solution(object):
    def shipWithinDays(self, weights, days):
        lower, higher = max(weights), sum(weights)

        def helper(capacity):
            day = 1
            onboard = 0
            for w in weights:
                onboard += w
                if onboard > capacity:
                    day += 1
                    onboard = w
               
            return day <= days

        while lower < higher:
            mid = (lower + higher) // 2
            if helper(mid):
                higher = mid
            else:
                lower = mid + 1
        
        return higher