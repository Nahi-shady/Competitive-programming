class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            expected = target - nums[i]
            if expected in nums and i != nums.index(expected):
                return [i, nums.index(expected)]