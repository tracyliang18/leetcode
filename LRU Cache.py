class Node(object):
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.len = 0
        self.cap = capacity
        self.kv_store = {}
        self.kn_store = {}

    def update(self, key):
        node = self.kn_store[key]
        if node is not self.tail:
            if node is self.head:
                self.head = node.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.kv_store:
            self.update(key)
            return self.kv_store[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.kv_store:
            self.kv_store[key] = value
            self.update(key)
        else:
            if self.len == self.cap:
                delete_key = self.head.key
                if self.cap == 1:
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                self.len -= 1
                del self.kv_store[delete_key]
                del self.kn_store[delete_key]

            node = Node(key)
            if not self.head:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.kn_store[key] = node
            self.kv_store[key] = value
            self.len += 1


cache = LRUCache(2)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print cache.get(1)
print cache.get(2)
cache.set(4,4)
print cache.get(2)
print cache.get(3)
