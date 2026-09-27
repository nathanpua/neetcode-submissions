# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def dfs(node, lowerbound, upperbound):
            if not node: return

            if not (lowerbound < node.val < upperbound):
                self.valid = False

            dfs(node.left, lowerbound, node.val)
            dfs(node.right, node.val, upperbound)

        dfs(root, float('-inf'), float('inf'))

        return self.valid
            