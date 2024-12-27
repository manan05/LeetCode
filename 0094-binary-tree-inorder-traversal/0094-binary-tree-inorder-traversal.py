# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return []
        
        def inorder(node):
            curr = node
            if curr.left is not None:
                inorder(curr.left)
            res.append(curr.val)
            if curr.right is not None:
                inorder(curr.right)
        
        inorder(root)
        return res