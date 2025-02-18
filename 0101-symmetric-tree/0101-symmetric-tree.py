# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val == r.val:
                if isMirror(l.right, r.left):
                    if isMirror(l.left, r.right):
                        return True
            return False
        return isMirror(root.left, root.right)