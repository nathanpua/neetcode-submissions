class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.cap = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        prevnode = self.tail.prev
        prevnode.next = node
        node.prev = prevnode
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = Node(val=value, key=key)
        self.insert(newnode)
        self.cache[key] = newnode

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
 