"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # # Approach 1: Using extra space - Hashmap
        # hashmap = {}
        # if not head:
        #     return None
        # curr = head
        # while curr:
        #     hashmap[curr] = Node(curr.val)
        #     curr = curr.next

        # temp = head
        # while temp:
        #     hashmap[temp].next = hashmap.get(temp.next)
        #     hashmap[temp].random = hashmap.get(temp.random)
        #     temp = temp.next

        # return hashmap[head]

        if not head:
            return None

        # New nodes create
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Remove the links from the og LL
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return new_head
