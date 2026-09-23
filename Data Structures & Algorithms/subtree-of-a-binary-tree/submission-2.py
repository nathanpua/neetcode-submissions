# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        # same tree function
        def isSame(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False

        # compare each node with the subroot, dfs to traverse tree and call isSame on each node
        def dfs(node):
            if not node: return 

            if isSame(node, subRoot): self.res = True

            left = dfs(node.left)
            right = dfs(node.right)
            

        dfs(root)
        return self.res
        
