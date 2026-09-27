# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_start = head
        dummy = ListNode(next=head)
        last = dummy
        for _ in range(k):
            if next_start:
                next_start = next_start.next
                last = last.next
            else: return head

        last.next = None
        prev = None
        tmp = head
        while tmp:
            nx = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nx
        
        head.next = self.reverseKGroup(next_start, k)

        return last