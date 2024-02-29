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
        def helper(root):
            nonlocal ans
            if not root:
                return
            stack.append(str(root.val))
            helper(root.left)
            helper(root.right)

            if not root.left and not root.right:
                ans += int(''.join(stack))
                stack.pop()
                return
            if stack[-1] == str(root.val):
                stack.pop()

        helper(root)
        return ans