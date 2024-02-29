# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,minn, maxx):
            if not node:
                return True
            if node.val <= minn or node.val >= maxx:
                # print(node.val < maxx,node.val,  maxx)
                return False

            return helper(node.left, minn, node.val) and helper(node.right, node.val, maxx)

        return helper(root, float('-inf'), float('inf'))