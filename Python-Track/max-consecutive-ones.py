class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        t = 0
        for i in nums:
            if i == 1:
                t += 1
            elif i == 0:
                t = 0
            if t > count:
                count = t
        count = max(t, count)
        return count