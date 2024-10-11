# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}
        i = 0
        curr = head
        while (curr is not None):
            if curr in hashmap:
                return curr
            hashmap[curr] = i
            i += 1
            curr = curr.next
        return None
