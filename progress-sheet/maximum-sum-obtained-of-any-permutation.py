class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = max(i[1] for i in requests)
        prefix = [0]*(n+2)

        for start, end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1 
        prefix = list(accumulate(prefix))

        nums.sort(reverse=True)
        prefix.sort(reverse=True)
        ans = 0
        for i in range(n+1):
            ans += prefix[i]*nums[i]

        return ans % (10**9 + 7)