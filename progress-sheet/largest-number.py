class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        print(nums)
        nums.sort(key=lambda arr: arr*10, reverse=True)
        if nums[0] == '0':
            return '0'
        print(nums)
        return ''.join(nums)