class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        prefix_sum = 0
        curr_sum = 0
        aligned = 0
        for i in range(len(flips)):
            prefix_sum += i+1
            curr_sum += flips[i]
            if prefix_sum == curr_sum:
                aligned += 1
        return aligned