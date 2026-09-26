# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while l2:
            nx = l2.next
            l2.next = prev
            prev = l2
            l2 = nx
        h2 = prev
        h1 = head
        while h2:
            h1_next = h1.next
            h2_next = h2.next
            h1.next = h2
            h2.next = h1_next
            h1 = h1_next
            h2 = h2_next
    