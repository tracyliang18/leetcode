class DisjointSet(object):
    def __init__(self, n):
        self.set = [-1 for i in range(n)]

    def find(self, index):
        path = []
        while self.set[index] >= 0:
            path.append(index)
            index = self.set[index]
        for ind in path:
            self.set[ind] = index
        self.show()
        return index


    def union(self, indexA, indexB):
        A = self.find(indexA)
        B = self.find(indexB)
        if A != B:
            if self.set[A] < self.set[B]:
                self.set[A] += self.set[B]
                self.set[B] = A
            else:
                self.set[B] += self.set[A]
                self.set[A] = B
        self.show()

    def show(self):
        print self.set

if __name__ == "__main__":
    disjointset = DisjointSet(7)
    disjointset.union(0,1)
    disjointset.union(1,4)
