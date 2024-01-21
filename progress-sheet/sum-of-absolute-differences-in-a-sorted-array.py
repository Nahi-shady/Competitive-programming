class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix =0
        total = sum(nums)
        ans = [0]*n

        for idx, val in enumerate(nums):
            ans[idx] = (2*idx - n)*val + total - prefix
            prefix += val
            total -= val
        return ans