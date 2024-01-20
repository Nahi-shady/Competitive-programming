class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter()
        ans, prefix = 0, 0
        count[0] = 1
        for i in nums:
            prefix += i
            remainder = prefix % k
            ans += count[remainder]
            count[remainder] += 1
        return ans