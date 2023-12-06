class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arranged = [0]*len(nums)
        p = 0
        n = 1
        for i in nums:
            if i < 0:
                arranged[n] = i
                n += 2
            else:
                arranged[p] = i
                p += 2

        return arranged