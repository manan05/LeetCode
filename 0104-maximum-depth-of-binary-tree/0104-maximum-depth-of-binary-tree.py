# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Top Down Approach
        # if root is None:
        #     return 0
        # res = 0
        # def helper(node, depth):
        #     nonlocal res
        #     if node is None:
        #         return
        #     # checking leaf node
        #     if node.left is None and node.right is None:
        #         res = max(res, depth)
        #     else:
        #         helper(node.left, depth + 1)
        #         helper(node.right, depth + 1)
        # helper(root, 1)
        # return res
        
        # # Bottom-up approach

        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1
        