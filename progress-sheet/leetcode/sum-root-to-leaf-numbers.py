# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = 0
        def helper(root, val):
            nonlocal ans
            if not root:
                return 
            if not root.left and not root.right:
                ans += int(val) + root.val
                print(ans, val)
                return 
            temp = str(int(val) + root.val) + '0'
            helper(root.left,  temp)
            helper(root.right, temp)
            

        helper(root, '0')
        return ans