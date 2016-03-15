class Graph(object):

    def DFS(self, source):
        raise NotImplementedError( "Should have implemented this" )

    def BFS(self, source):
        raise NotImplementedError( "Should have implemented this" )


class Graph_adjacency_list(Graph):
    def __init__(self, n, connect_info, isdirected):
        self.adjlist = [[] for i in range(n)]
        for info in connect_info:
            s,t,w = info
            self.adjlist[s].append({"weight":w, "target" : t})
            if not isdirected:
                self.adjlist[t].append({"weight":w, "target" : s})
