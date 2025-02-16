from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # if root is None:
        #     return []

        # def helper(node, level):
        #     # base case
        #     if len(res) == level:
        #         res.append([])

        #     res[level].append(node.val)

        #     if node.left is not None:
        #         helper(node.left, level + 1)
        #     if node.right is not None:
        #         helper(node.right, level + 1)
    
        # helper(root, 0)
        # return res

        # iteratively
        res = []
        if root is None:
            return []
        queue = deque([root,])
        level = 0
        while queue:
            res.append([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                res[level].append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            level += 1
        return res