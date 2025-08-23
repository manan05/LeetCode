# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Recursion
        # # base case
        # if not head or not head.next:
        #     return head
        
        # last_elem = self.reverseList(head.next)

        # # self work
        # next_elem = head.next
        # next_elem.next = head
        # head.next = None

        # return last_elem

        # Iterative
        prev = None
        curr = head
        while curr:
            next_elem = curr.next
            curr.next = prev
            prev = curr
            curr = next_elem
        return prev
