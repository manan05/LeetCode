# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Approach 1: Using additional space O(N)
        # res = []
        # curr = head
        # while curr:
        #     res.append(curr)
        #     curr = curr.next
        
        # return res[len(res) // 2]

        # # Without any additional space
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow