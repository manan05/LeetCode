# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Brute Force - using additional space
        # hashset = set()
        # if not head:
        #     return
        # curr = head
        # while curr:
        #     if curr in hashset:
        #         return curr
        #     hashset.add(curr)
        #     curr = curr.next

        # # Approach 2: no extra memory
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
