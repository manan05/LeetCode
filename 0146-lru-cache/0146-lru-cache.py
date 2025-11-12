class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to nodes
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        curr = ListNode(key, value)
        self.cache[key] = curr
        self.insert(curr)

        if len(self.cache) > self.capacity:
            delete = self.left.next
            self.remove(delete)
            del self.cache[delete.key]


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev_end = self.right.prev
        prev_end.next = node
        self.right.prev = node
        node.prev = prev_end
        node.next = self.right
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)