class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, left, longest = 0, 0, 0

        for r in range(len(nums)):
            if not nums[r]:
                zeros += 1
            while zeros > k:
                if not nums[left]:
                    zeros -= 1
                left += 1
            longest = max(longest, r-left + 1)

        return longest