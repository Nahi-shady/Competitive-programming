# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def helper(root):
            nonlocal ans
            if not root:
                return (inf, -inf)

            l_min, l_max = helper(root.left)
            r_min, r_max = helper(root.right)

            min_val = min(l_min,r_min)
            max_val = max(l_max, r_max)
            if min_val < inf and max_val > -inf:    
                ans = max(abs(root.val - min_val), abs(root.val - max_val), ans)

            return (min(root.val, min_val), max(root.val, max_val))
        
        helper(root)
        return ans