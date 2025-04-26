# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Recursion

        # # base case
        # if head is None or head.next is None:
        #     return head

        # right = self.reverseList(head.next)

        # temp = head.next
        # temp.next = head
        # head.next = None

        # return right

        # # Iteratively
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

