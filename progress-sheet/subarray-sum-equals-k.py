class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        count = 0
        for i in prefix:
            count += freq[i-k]
            freq[i] += 1
        return count