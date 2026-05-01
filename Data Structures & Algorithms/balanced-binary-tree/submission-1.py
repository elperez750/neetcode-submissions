# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node == None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left-right) > 1:
                raise Exception("unbalanced")

            return 1 + max(left, right)


        try:


            dfs(root)
            return True
        except:
            return False

