# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def dfs(node, i):
            if not node:
                return
            
            levels[i].append(node.val)

            dfs(node.left, i+1)
            dfs(node.right, i+1)

        dfs(root, 0)
        ans = []
        flag = True
        for i, val in levels.items():
            if flag:
                ans.append(val)
                flag = False
            else:
                ans.append(val[::-1])
                flag = True
        return ans