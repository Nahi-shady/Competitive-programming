# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        ans = 0
        def helper(root):
            nonlocal curr, k, ans
            if not root: return 

            helper(root.left)
            curr += 1
            if curr == k:
                ans = root.val
                return 
            helper(root.right)
        
        helper(root)

        return ans