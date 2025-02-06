# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Approach 1: Recursive
        # if root is None:
        #     return []
        # res = []

        # def helper(curr):
        #     if curr.left is not None:
        #         helper(curr.left)
        #     if curr.right is not None:
        #         helper(curr.right)
        #     res.append(curr.val)

        # helper(root)
        # return res

        # # Approach 2: 2 Stack method
        # res = []
        # if root is None:
        #     return res
        
        # pathStack = []
        # mainStack = [root, ]

        # while(mainStack):
        #     curr = mainStack[-1]

        #     if pathStack and pathStack[-1] == curr:
        #         res.append(curr.val)
        #         mainStack.pop()
        #         pathStack.pop()
        #     else:
        #         pathStack.append(curr)
        #         if curr.right is not None:
        #             mainStack.append(curr.right)
        #         if curr.left is not None:
        #             mainStack.append(curr.left)
        # return res

        # Approach 3: Rearranging PreOrder
        if root is None:
            return []
        res = []
        stack = [root, ]
        while(stack):
            curr = stack.pop()
            res.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        res.reverse()
        return res



        
