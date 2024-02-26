class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {nums2[i]: i for i in range(len(nums2))}
        ans = [-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                ans[top] = i
            stack.append(i)
            
        res = []
        for val in nums1:
            if ans[hash[val]] == -1:
                res.append(-1)
            else:
                res.append(nums2[ans[hash[val]]])
        # print(ans, hash)
        return res