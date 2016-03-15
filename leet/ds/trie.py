class Node(object):
    def __init__(self):
        self.next = {}
        self.key = None
        self.isend = False

    def _print(self):
        print self.key,self.isend

class Trie(object):
    def __init__(self, word_list):
        self.root = Node()
        self.root.key = ""
        self.root.isend = False

        for word in word_list:
            cur = self.root
            if len(word) > 0:
                for c in word:
                    if c in cur.next:
                        cur = cur.next[c]
                    else:
                        cur.next[c] = Node()
                        cur.next[c].key = cur.key + c
                        cur = cur.next[c]
                cur.isend = True

    def show(self):
        import Queue
        queue = Queue.Queue()
        queue.put(self.root)
        while not queue.empty():
            cur = queue.get()
            for child in cur.next:
                cur.next[child]._print()
                queue.put(cur.next[child])
    

trie = Trie(["show","shaw"])
trie.show()
