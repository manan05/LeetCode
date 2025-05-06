# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # calculate length
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        # if k > length
        k = k % length
        if k == 0:
            return head

        # finding the new head
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        curr.next = head

        return new_head

