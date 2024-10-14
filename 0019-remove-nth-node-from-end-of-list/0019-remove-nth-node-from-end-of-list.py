# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode(0) # default dummy node
        curr.next = head
        i = 0
        first = head
        while (first is not None):
            i += 1
            first = first.next
        i = i - n
        first = curr
        while i > 0:
            i -= 1
            first = first.next
        first.next = first.next.next
        return curr.next
