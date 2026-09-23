# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, parent):
            if not node:
                return

            if node.val >= parent:
                self.count += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            
            else:
                dfs(node.left, parent)
                dfs(node.right, parent)
        
        dfs(root, float('-inf'))
        return self.count