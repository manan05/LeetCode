# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        def helper(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left is not None:
                helper(node.left, level + 1)
            if node.right is not None:
                helper(node.right, level + 1)
        helper(root, 0)
        return res