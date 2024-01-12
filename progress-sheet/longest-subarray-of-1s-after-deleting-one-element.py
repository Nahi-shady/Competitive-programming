class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        longest = 0
        curr = 0
        left = 0
        for i in range(len(nums)):
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                else:
                    curr -= 1
                left += 1
            if nums[i] == 0:
                zeros += 1
            else:
                curr += 1
            longest = max(longest, curr)


        return longest-1 if zeros == 0 else longest