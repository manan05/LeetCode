# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # but the below code is 2 pass meaning we have to move through the LL twice
        # curr = ListNode(0) # default dummy node
        # curr.next = head
        # i = 0
        # first = head
        # while (first is not None):
        #     i += 1
        #     first = first.next
        # i = i - n
        # first = curr
        # while i > 0:
        #     i -= 1
        #     first = first.next
        # first.next = first.next.next
        # return curr.next

        # One pass algorithm
        zeroth = ListNode(0)
        zeroth.next = head
        first, second = zeroth, zeroth
        # move the first to n 
        for _ in range(n + 1):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return zeroth.next