
class CacheNode:
    def __init__(self,key):
        self.key  = key
        self.prev = None
        self.next = None


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cacheLen = 0
        self.cacheNodeList = None

    def insertToHead(self, cachenode):
        if self.cacheNodeList == cachenode:
            return
        if self.cacheNodeList == None:
            self.cacheNodeList = cachenode
            self.cacheNodeList.next = cachenode
            self.cacheNodeList.prev = cachenode
            return

        if cachenode.prev != None:
            cachenode.prev.next = cachenode.next
            cachenode.next.prev = cachenode.prev
        cachenode.next = self.cacheNodeList
        cachenode.prev = self.cacheNodeList.prev
        self.cacheNodeList.prev.next = cachenode
        self.cacheNodeList.prev = cachenode
        self.cacheNodeList = cachenode

    def removeLastNode(self):
        key = self.cacheNodeList.prev.key
        #print "remove key should be second",key
        if self.cacheLen == 1:
            self.cacheNodeList = None
        else:
            # print self.cacheNodeList.prev.key
            # print self.cacheNodeList.key
            # print self.cacheNodeList.next.key
            self.cacheNodeList.prev.prev.next = self.cacheNodeList
            self.cacheNodeList.prev = self.cacheNodeList.prev.prev

            # print self.cacheNodeList.prev.key
            # print self.cacheNodeList.key
            # print self.cacheNodeList.next.key
        del self.cache[key]
        #print "remove last node"
        self.cacheLen -= 1
        #self.printList()
        #self.printList()

    def printList(self):
        print "print list order"
        head = self.cacheNodeList
        p = head
        i=0
        while i < self.cacheLen * 2:
            print p.key,self.cache[p.key][0]
            i += 1
            p=p.next
        print ""

    def printListReverse(self):
        print "print list reverse order"
        p = self.cacheNodeList.prev
        i=0
        while i < self.cacheLen * 2:
            print p.key,self.cache[p.key][0]
            i += 1
            p=p.prev
        print ""


    # @return an integer
    def get(self, key):
        if key in self.cache:
            cachenode = self.cache[key][1]
            self.insertToHead(cachenode)
            #self.printList()
            #self.printListReverse()
            return self.cache[key][0]

        else:
            return -1



    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.capacity == 0:
            return
        if self.get(key) != -1:
            self.cache[key][0] = value
        else:
            if self.cacheLen >= self.capacity:
                self.removeLastNode()
            cacheNode = CacheNode(key)
            self.insertToHead(cacheNode)
            self.cache[key] = [value,cacheNode]
            self.cacheLen += 1
        #self.printList()
        #self.printListReverse()
        #print self.cache


#print [0,1,1].extend([2,3,4])
lruCache = LRUCache(3)
#print "set 1"
lruCache.set("first",1)
#print "set 2"
lruCache.set("second",2)
#print "set 3"
lruCache.set("third",3)
#print "get 1"
print lruCache.get("first")
#print "set 3"
lruCache.set("third",33)
#print "set 4"
lruCache.set("fourth",4)



