# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # Approach 1: Using Space and recursion``
        # def reverseLinkList(head, k):
        #     prev = None
        #     curr = head
        #     while k > 0:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp
        #         k -= 1
        #     return prev

        # i = 0
        # curr = head
        # while i < k and curr:
        #     curr = curr.next
        #     i += 1
        # if i == k:
        #     # reverse the current group
        #     reversedHead = reverseLinkList(head, k)

        #     # recursively reverse the other as well
        #     head.next = self.reverseKGroup(curr, k)
        #     return reversedHead
        # return head

        def reverseLL(head, k):
            prev = None
            curr = head
            while k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k -= 1
            return prev

        curr = head
        new_head = None
        tail = None
        while curr:
            count = 0
            while count < k and curr:
                curr = curr.next
                count += 1
            if count == k:
                reversedHead = reverseLL(head, k)
                if not new_head:
                    new_head = reversedHead
                if tail:
                    tail.next = reversedHead
                tail = head
                head = curr
        if tail:
            tail.next = head

        return new_head
