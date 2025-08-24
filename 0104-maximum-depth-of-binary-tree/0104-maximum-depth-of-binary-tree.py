# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_len):
            if node is None:
                return curr_len

            left_len = dfs(node.left, curr_len + 1)
            right_len = dfs(node.right, curr_len + 1)

            return max(left_len, right_len)

        return dfs(root, 0)
