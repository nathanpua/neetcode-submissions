# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Options are: node itself, node + left tree, node + right tree, node + both tree
            self.res = max(self.res, node.val, node.val + left, node.val + right, node.val + left + right)

            # when returning to parent only choose 1 path - Left or right or none
            return node.val + max(left, right, 0)

        dfs(root)

        return self.res

