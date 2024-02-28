# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def helper(node):
            if not node:
                return 
            freq[node.val] += 1
            helper(node.left)
            helper(node.right)
        helper(root)
        mode = max(freq.values())
        print(freq, mode)
        return [i for i, v in freq.items() if v==mode]