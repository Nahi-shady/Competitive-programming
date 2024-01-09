class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        pivot = 1
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == pivot:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1