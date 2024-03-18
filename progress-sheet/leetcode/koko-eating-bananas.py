class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 0, max(piles)
        while l + 1 < r:
            mid = (l+r)//2
            hour = 0
            for pile in piles:
                if pile <= mid:
                    hour += 1
                else:
                    hour = hour + (pile//mid)
                    if pile % mid:
                        hour += 1
                
                

            if hour > h:
                l = mid
            elif hour <= h:
                r = mid
            # print(l, r,mid, hour)
        
        return r