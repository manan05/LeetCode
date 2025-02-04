# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive
        # res = []
        # if root is None:
        #     return res

        # def helper(curr):
        #     if curr is None:
        #         return
        #     res.append(curr.val)
        #     helper(curr.left)
        #     helper(curr.right)
        # helper(root)
        # return res

        # iterative
        if root is None:
            return []
        stack = [root,]
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)

        return res
