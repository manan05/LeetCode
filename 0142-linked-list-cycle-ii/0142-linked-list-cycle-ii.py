# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        if not head:
            return
        i = 0
        curr = head
        while curr:
            if curr in hashset:
                return curr
            hashset.add(curr)
            curr = curr.next
            i += 1