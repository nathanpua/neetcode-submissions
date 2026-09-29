# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        if root: q.append(root)
        res = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else: res += 'N'
        
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        cache = {}
        data = data.split(',')

        if data[0] == "": return None

        for i in range(len(data)):
            if data[i] != 'N':
                cache[i] = TreeNode(val=int(data[i]))

        child_idx = 1
        # observe left child is next idx, right child is next next idx
        for i in range(len(data)):
            if data[i] == 'N': continue 
            # Assign left child and move pointer
            if child_idx in cache:
                cache[i].left = cache[child_idx]
            child_idx += 1
            
            # Assign right child and move pointer
            if child_idx in cache:
                cache[i].right = cache[child_idx]
            child_idx += 1

        return cache[0]
        # print(data)
        # for (k, v) in cache.items():
        #     print(k, ' : ', v.val)