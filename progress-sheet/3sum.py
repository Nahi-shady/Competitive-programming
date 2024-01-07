class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr = nums[left] + nums[right]

                if curr + nums[i] == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
      
        return list(triplets)
        