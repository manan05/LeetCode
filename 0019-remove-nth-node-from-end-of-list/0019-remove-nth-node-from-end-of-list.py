# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # 2 Pass algo
        # size = 0
        # prev = ListNode(0)
        # prev.next = head
        # curr = head
        # while curr:
        #     size += 1
        #     curr = curr.next
        # idx = size - n
        # curr = prev
        # while curr:
        #     if idx == 0:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        #     idx -= 1
        # return prev.next

        # # One Pass
        prevNode = ListNode(0)
        prevNode.next = head
        first, second = prevNode, prevNode
        while first:
            if n >= 0:
                first = first.next
            else:
                first = first.next
                second = second.next
            n -= 1
        second.next = second.next.next
        return prevNode.next
