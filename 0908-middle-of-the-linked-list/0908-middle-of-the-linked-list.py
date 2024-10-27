# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively:
        i = head
        j = head

        while j.next is not None and j is not None and j.next.next is not None:
            i = i.next
            j = j.next.next
        if (j.next is None):
            return i
        return i.next