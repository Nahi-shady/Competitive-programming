class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        pairs = 0
        for i in count.keys():
            val = count[i]
            if val > 1:
                pairs += val*(val-1) // 2
        return pairs