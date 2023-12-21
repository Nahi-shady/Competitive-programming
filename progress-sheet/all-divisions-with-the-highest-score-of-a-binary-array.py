class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_one = nums.count(1)
        freq = {}

        zeros, ones = 0, 0
        max_sum = 0
        for i in range(len(nums)):
            temp = zeros + (count_one - ones)
            freq[i] = temp
            max_sum = max(max_sum, temp)
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
        freq[i+1] = zeros + (count_one - ones)
        max_sum = max(max_sum, freq[i+1])

        return [i for i in freq if freq[i] == max_sum]