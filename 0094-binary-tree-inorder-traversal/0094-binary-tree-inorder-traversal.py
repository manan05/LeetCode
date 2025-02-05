# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursive

        # if root is None:
        #     return []
        # res = []

        # def helper(curr):
        #     if curr is None:
        #         return
        #     helper(curr.left)
        #     res.append(curr.val)
        #     helper(curr.right)

        # helper(root)
        # return res

        # iterative
        if root is None:
            return []
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res