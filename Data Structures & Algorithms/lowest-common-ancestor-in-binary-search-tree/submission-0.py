# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        if not node:
            return False
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        curr = node == q or node == p

        if (left and right) or (left and curr) or (right and curr):
            if self.res == None:
                self.res = node

        return curr or left or right