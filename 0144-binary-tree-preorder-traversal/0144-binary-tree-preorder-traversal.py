# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursively

        ans = []
        def preorder(curr):
            #base case
            if(curr is None):
                return
            
            ans.append(curr.val)
            preorder(curr.left)
            preorder(curr.right)
        
        preorder(root)
        return ans
        