class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [i % 2 for i in nums]
        prefix_counts = [0]*(len(nums)+1)
        prefix_counts[0] = 1
        odd_count = answer = 0

        for num in nums:
            if num:
                odd_count += 1
            if odd_count >= k:
                answer += prefix_counts[odd_count-k]
                
            prefix_counts[odd_count] += 1

        return answer