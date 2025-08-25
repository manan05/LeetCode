# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, res):
            if node is None:
                return 

            if node.left:
                inorder(node.left, res)
            res.append(node.val)
            if node.right:
                inorder(node.right, res)
            return res
        return inorder(root, [])[k - 1]
