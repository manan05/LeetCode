# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iteratively
        # prev = None
        # curr = head
        # while(curr is not None):
        #     front = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = front
        # return prev

        # Recursively

        if (head is None) or (head.next is None):
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead