# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1

        dummy = ListNode(0)
        cur = dummy
        while heap:
            smallest, count, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))

        return dummy.next