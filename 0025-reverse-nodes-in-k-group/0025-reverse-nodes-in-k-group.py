# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # Approach 1: Recursion
        def reverseLinkList(head, k):
            prev = None
            curr = head
            while k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                k -= 1
            return prev
        
        i = 0
        curr = head
        while i < k and curr:
            curr = curr.next
            i += 1
        if i == k:
            reversedHead = reverseLinkList(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reversedHead
        return head
