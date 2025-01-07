from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # Recursive:
        # if root is None:
        #     return []
        # res = []
        # def helper(node, level):
        #     if len(res) == level:
        #         res.append([])
        #     res[level].append(node.val)
        #     if node.left is not None:
        #         helper(node.left, level + 1)
        #     if node.right is not None:
        #         helper(node.right, level + 1)
        # helper(root, 0)
        # return res

        # Iterative
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque(
            [
                root,
            ]
        )

        while queue:
            levels.append([])
            length = len(queue)
            for i in range(length):
                nn = queue.popleft()
                levels[level].append(nn.val)

                if nn.left:
                    queue.append(nn.left)
                if nn.right:
                    queue.append(nn.right)
            level += 1
        return levels
