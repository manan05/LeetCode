# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # returns the max path WITHOUT split
        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(0, left_max)
            right_max = max(0, right_max)

            # max path WITH SPLT
            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)
        dfs(root)
        return res[0]
