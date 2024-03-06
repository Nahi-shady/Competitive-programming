class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid
        
        start = l if nums[l] == target else -1
        end = left if nums[left] == target else -1

        return [start, end]
        