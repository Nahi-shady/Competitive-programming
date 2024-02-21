class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = len(nums)
        unreach = 1
        patch = i = 0
        while unreach <= n:
            if i < m and unreach >= nums[i]:
                unreach +=  nums[i]
                i += 1
            else:
                unreach *= 2
                patch += 1
        return patch