class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        pointer = 0
        ans = []
        while pointer <= len(nums)-2:
            ans += [nums[pointer+1]]*nums[pointer]
            pointer += 2
            
        return ans