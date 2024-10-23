# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # base case
        # if (head is None or head.next is None):
        #     return head
        
        # # init nodes
        # fnode = head
        # snode = head.next
        
        # # swap with recursive call
        # fnode.next = self.swapPairs(snode.next)
        # snode.next = fnode
        
        # return snode

        # iterative
        
        prev = ListNode(0)
        dummy = prev
        prev.next = head

        while(head and head.next):

            # nodes init
            fnode = head
            snode = head.next

            # swapping
            prev.next = snode
            fnode.next = snode.next
            snode.next = fnode
            
            #make head correct
            prev = fnode
            head = fnode.next
        return dummy.next

