#
class BinaryMaxHeap(object):
    def __init__(self,array):
        self.array = array
        self.heapify(self.array)


    def heapify(self,array):
        n = len(array) - 1
        #start from array[n/2] which has children at the bottom of the tree, adjust from bottom to up
        for index in range((n - 1)/2, -1, -1):
            self._siftdown(index)

    def _siftup(self, index):
        parent = (index - 1) / 2
        if parent >= 0:
            if self.array[index] > self.array[parent]:
                self.array[index], self.array[parent] = self.array[parent], self.array[index]
                self._siftup(parent)

    def _siftdown(self,index):
        child = index * 2 + 1
        if child >= len(self.array):
            return
        if child + 1 < len(self.array):
            if self.array[child+1] > self.array[child]:
                child = child + 1
        if self.array[index] < self.array[child]:
            self.array[index],self.array[child] = self.array[child], self.array[index]
            self._siftdown(child)

    def Max(self):
        if len(self.array) > 0:
            return self.array[0]
        else:
            return None

    def pop(self):
        if len(self.array) > 0:
            self.array[0] = self.array[-1]
            del self.array[-1]
            self._siftdown(0)

    def push(self, val):
        self.array.append(val)
        self._siftup(len(self.array) - 1)

    def replace_key(self, index, val):
        prev = self.array[index]
        self.array[index] = val

        if val < prev:
            self._siftdown(index)
        else:
            self._siftup(index)


def test():
    maxheap = BinaryMaxHeap([1,3,5,7,9,11])
    print maxheap.Max()
    maxheap.pop()
    print maxheap.Max()
    maxheap.replace_key(0, 0)
    print maxheap.Max()
    print maxheap.array

def heapq_test():
    import heapq
    array = [1,3,5,7,9,11]
    array = map(lambda x:-x, array)
    heapq.heapify(array)
    print -array[0]
    heapq.heappop(array)
    print -array[0]
    heapq.heappush(array,-100)
    print -array[0]

heapq_test()
