class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix, prefix = [1], [1]
        for i in range(n):
            prefix.append(prefix[-1] * nums[i])
            postfix.append(postfix[-1] * nums[-(i+1)])
        postfix = postfix[::-1]
        ans = []
        
        for i in range(n-1):
            if i == 0:
                ans.append(postfix[1])
            else:
                ans.append(prefix[i]*postfix[i+1])
        ans.append(prefix[n-1])
        return ans