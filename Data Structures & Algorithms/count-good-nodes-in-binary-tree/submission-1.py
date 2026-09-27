# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        # parent tracks the maximum in that path
        def dfs(node, parent):
            if not node: return

            if node.val >= parent:
                parent = node.val
                self.good += 1
            
            dfs(node.left, parent)
            dfs(node.right, parent)

        dfs(root, float('-inf'))

        return self.good
            