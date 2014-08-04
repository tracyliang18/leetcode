from listmodule import *

class my_deque:
    def __init__(self, maxn):
        self.length = maxn
        self.left = 0
        self.right = 0
        self.queue = [None for x in xrange(maxn)]
        self.curlen = 0

    def isempty(self):
        return self.curlen == 0

    def isfull(self):
        return not (self.curlen < self.length)

    def expand(self):
        i = 0
        newqueue = []
        while i < self.length:
            newqueue.append(self.queue[self.left])
            self.left = (self.left + 1) % self.length
            i += 1
        self.queue = newqueue * 2
        self.length += self.length
        self.left = 0
        self.right = self.curlen

    def append(self, val):
        if self.isfull():
            self.expand()
        self.queue[self.right] = val
        self.right = (self.right + 1) % self.length
        self.curlen += 1
        #print self.queue

    def pop(self):
        if self.isempty():
            return None
        self.right = (self.right + self.length - 1) % self.length
        v = self.queue[self.right]
        self.curlen -= 1
        #print self.queue
        return v

    def popleft(self):
        if self.isempty():
            return None
        v = self.queue[self.left]
        self.left = (self.left + 1) % self.length
        self.curlen -= 1
        #print self.queue
        return v
    def appendleft(self,val):
        if self.isfull():
            self.expand()
        self.left = (self.left + self.length - 1) % self.length
        self.queue[self.left] = val
        self.curlen += 1
        #print self.queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:
            return None
        q = my_deque(100)
        p = head
        while p:
            q.append(p)
            p = p.next
        p = q.popleft()
        head = p
        while True:
            cur = q.pop()
            if cur:
                p.next = cur
                p = p.next
            else:
                break

            cur = q.popleft()
            if cur:
                p.next = cur
                p = p.next
            else:
                break
        p.next = None
        return head

a = makelist([1,2,3,4,5])
so = Solution()
l = so.reorderList(a)
printlist(l)
