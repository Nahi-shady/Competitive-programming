# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return [0, float('inf'), float('-inf'), True]
            
            left, l_minn, l_maxx, l_bst = dfs(node.left)
            right, r_minn, r_maxx, r_bst = dfs(node.right)

            cur = left + node.val + right
            minn = min(l_minn, r_minn, node.val)
            maxx = max(l_maxx, r_maxx, node.val)

            bst = False
            if l_bst and r_bst and l_maxx < node.val < r_minn:
                cur = left + node.val + right
                ans = max(ans, cur)
                bst = True


            return [cur, minn, maxx, bst]



        dfs(root)
        
        return ans