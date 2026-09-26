"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {}
        if not head: return None
        cur = head

        while cur:
            cache[cur] = Node(x=cur.val, next=None, random=None)
            cur=cur.next

        for original, copy in cache.items():
            copy.next = cache.get(original.next, None)
            copy.random = cache.get(original.random, None)
        
        return cache[head]