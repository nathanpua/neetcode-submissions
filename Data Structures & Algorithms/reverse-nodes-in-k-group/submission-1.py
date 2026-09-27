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

        # set next_start to start of next group
        # set last to last in the group (1 node behind next_start)
        for _ in range(k):
            if next_start:
                next_start = next_start.next
                last = last.next
            else: return head

        # break off the group with last.next = None, so we can reverse this group
        last.next = None
        prev = None
        tmp = head
        while tmp:
            nx = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nx
        
        # head is now last in group, and last is the new head
        # recusively call the function on next_start and link it to the tail (head)
        head.next = self.reverseKGroup(next_start, k)

        return last