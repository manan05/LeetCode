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
        if not head:
            return None
        hashmap = {}
        curr = head
        while curr:
            if curr not in hashmap:
                hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hashmap[curr].next = hashmap.get(curr.next, None)
            hashmap[curr].random = hashmap.get(curr.random, None)
            curr = curr.next
        return hashmap[head]
