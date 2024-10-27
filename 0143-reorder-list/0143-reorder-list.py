# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if(not head):
            return
        # finding middle node
        i = j = head
        while(j and j.next):
            i = i.next
            j = j.next.next
        
        # i will have middle Node

        # reverse the second part

        prev = None
        curr = i

        while(curr):
            # prev to curr
            # curr = curr.next
            # curr next to prev
            front = curr.next

            curr.next = prev
            prev = curr
            curr = front
        
        # prev = front node
        
        # merging step

        f, s = head, prev
        while(s.next):
            dummy = f.next
            f.next = s
            f = dummy

            dummy = s.next
            s.next = f
            s = dummy
    

