# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        ------p-----q-----
        we have 3 cases where root can be:
        1. root.val < min(p.val, q.val) => we need to find smaller => go left
        2. root.val > max(p.val, q.val) => we need to find larger => go right
        3. root.val between p.val and q.val => valid, we can return this
        """
        while root:
            if root.val > max(p.val,q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                return root
