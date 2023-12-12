class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for i in nums:
            if i-1 in lookup:
                continue
            curr_range = i+1
            while curr_range in lookup:
                curr_range += 1
            
            longest = max(curr_range-i, longest)
    
        return longest