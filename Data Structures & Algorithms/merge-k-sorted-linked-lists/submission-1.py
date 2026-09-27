# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        use a min heap to keep the smallest value at the root
        push all head nodes into the heap
        min heap contains (node.val, tie-breaker (count), node)
        tie breaker to ensure we dont compare on node if node.val are same in the heap
        """
        heap = []
        count = 0

        # pushing all head nodes into heap, skip empty lsts
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1
        # build the sorted using dummy node
        dummy = ListNode(0)
        cur = dummy
        # heap always has the list with smallest node val on top. pop it, and add node.next to heap
        while heap:
            smallest, count, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))

        return dummy.next