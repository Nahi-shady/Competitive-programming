class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder, seeker = 0, 0
        while seeker < len(nums):
            if nums[seeker] > nums[holder]:
                holder += 1
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            seeker += 1
            
        return holder + 1
            
            