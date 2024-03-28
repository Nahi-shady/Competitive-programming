class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        l, r = 0, 0
        maxx = 0
        curr_freq = defaultdict(int)
        
        while r < len(nums):
            curr_freq[nums[r]] += 1
            while curr_freq[nums[r]] > k:
                curr_freq[nums[l]] -= 1
                l += 1

            maxx = max(maxx, r-l + 1)
            r += 1

        return maxx