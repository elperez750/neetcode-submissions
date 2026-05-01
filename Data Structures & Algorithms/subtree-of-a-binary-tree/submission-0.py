# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return False
            
        tree_equal = self.isTreeEqual(root, subRoot)
        
        if tree_equal:
            return True

        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isTreeEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if (root == None) != (subRoot == None):
            return False
        

        if root.val == subRoot.val:
            left_subtree = self.isTreeEqual(root.left, subRoot.left)
            right_subtree = self.isTreeEqual(root.right, subRoot.right)
            return left_subtree and right_subtree




        
    



