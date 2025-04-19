# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(res, curr):
            if curr is None:
                return

            if curr.left is not None:
                inorder(res, curr.left)
            res.append(curr.val)
            if curr.right is not None:
                inorder(res, curr.right)

        res = []
        inorder(res, root)

        left, right = 0, len(res) - 1
        while left < right:
            mSum = res[left] + res[right]
            if mSum == k:
                return True
            elif mSum > k:
                right -= 1
            else:
                left += 1
        return False