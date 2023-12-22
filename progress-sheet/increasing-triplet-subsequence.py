class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        last = nums[-1]
        maxs = []
        for i in nums[::-1]:
            last = max(i, last)
            maxs.append(last)
        maxs.reverse()

        first = nums[0]
        mins = []
        for i in nums:
            first = min(i, first)
            mins.append(first)

        mins[0] = float('inf')
        maxs[-1] = -float('inf')
        print(mins, maxs)
        for i in range(len(nums)):
            if mins[i] < nums[i] < maxs[i]:
                return True

        return False