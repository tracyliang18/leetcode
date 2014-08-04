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
        print self.queue

    def pop(self):
        if self.isempty():
            return None
        self.right = (self.right + self.length - 1) % self.length
        v = self.queue[self.right]
        self.curlen -= 1
        print self.queue
        return v

    def popleft(self):
        if self.isempty():
            return None
        v = self.queue[self.left]
        self.left = (self.left + 1) % self.length
        self.curlen -= 1
        print self.queue
        return v
    def appendleft(self,val):
        if self.isfull():
            self.expand()
        self.left = (self.left + self.length - 1) % self.length
        self.queue[self.left] = val
        self.curlen += 1
        print self.queue

q = my_deque(3)
q.append(1)
q.append(2)
print q.pop()#2
q.append(3)
print q.popleft()#1
q.appendleft(8)
q.appendleft(9)
q.append(10)
print q.pop()
print q.pop()
print q.pop()
print q.pop()


