class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n, prefix, freq = len(nums), 0, defaultdict(int)
        freq[0] = 1
        ans = 0
        for i in range(n):
            prefix += nums[i]
            ans += freq[prefix-goal]
            freq[prefix] += 1

        return ans