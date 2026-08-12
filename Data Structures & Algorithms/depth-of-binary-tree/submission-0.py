# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepthHelper(1, root.right), self.maxDepthHelper(1, root.left))

    def maxDepthHelper(self, depth: int, root:Optional[TreeNode]):
        if root == None:
            return depth
        
        depth = depth + 1
        return max(self.maxDepthHelper(depth, root.right), self.maxDepthHelper(depth, root.left))
        