# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        curr = False
        if root.val == subRoot.val:
            curr = self.isEqual(root, subRoot)
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right or curr

    def isEqual(self, one, two):
        if not one and not two:
            return True
        if not one or not two:
            return False
        
        if one.val != two.val:
            return False
        
        left = self.isEqual(one.left, two.left)
        right = self.isEqual(one.right, two.right)

        return left and right
