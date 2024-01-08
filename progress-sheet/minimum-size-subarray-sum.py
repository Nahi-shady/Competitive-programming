class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        l , tot = 0, 0
        for r in range(len(nums)):
            tot += nums[r]
            while target <= tot:
                ans = min(ans, r - l + 1)
                tot -= nums[l]
                l += 1
                
        return 0 if ans > len(nums) else ans
