# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # recursion
        # res = []
        
        # def preorder(node):
        #     if node is None:
        #         return
        #     res.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        
        # preorder(root)
        # return res
        
        # # using stack
        # if root is None:
        #     return []

        # stack = [root,]
        # res = []

        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     if(curr.right is not None):
        #         stack.append(curr.right)
        #     if(curr.left is not None):
        #         stack.append(curr.left)
        
        # return res

        # Morris Traversal
        node = root
        output = []

        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                pred = node.left

                while pred.right and pred.right is not node:
                    pred = pred.right
                
                if not pred.right:
                    output.append(node.val)
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None
                    node = node.right
        return output
