class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = sum(nums[:k])/k
        average = curr_avg
        left = 0
        for i in range(k, len(nums)):
            left_num = nums[left]
            curr_avg = curr_avg + (nums[i] - left_num)/k
            average = max(average, curr_avg)
            
            left += 1
            
        return average