# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        if p.val <= root.val <= q.val:
            return root
        if root.val > p.val and root.val > q.val:
            # explore left
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            # explore right
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        
        