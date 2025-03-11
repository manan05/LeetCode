# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def helper(curr):
            nonlocal total_sum

            if not curr:
                return 0

            rightS = helper(curr.right)
            leftS = helper(curr.left)
            tilt = abs(rightS - leftS)

            total_sum += tilt

            return leftS + rightS + curr.val
        
        helper(root)
        return total_sum