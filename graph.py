# bfs graph traversal:
# Need adjacency-list representation of a graph.
#
class Vertex:
    def __init__(self, vName):
        self.adjList = []
        self.vtx = vName

    @classmethod
    def newV(cls, vName):
        vee = cls(vName)
        return vee
    
    def adjAdd(self, adjList):
        for i in adjList:
            self.adjList.append(i)
        return self

class Graph:
    def __init__(self):
        self.nodes = {}

    def vtxAdd(self, vtx):
        self.nodes[vtx.vtx] = vtx
        return self

    @classmethod
    def gBuild(cls, vList):
        gee = cls()
        for i in vList:
            gee.vtxAdd(i)
        return gee

    def bfs(self, startVtx):
        """Performs breadth-first-search of the graph, building a list
of vertices to return, which provides a breath-first-ordering of the
vertices in the graph."""
        currV = None
        queue = [startVtx] # the "what to visit next"
        seen = {}  # set of seen vertices, as a dictionary
        # append to back, pop off front
        while(len(queue) != 0):
            currV = queue.pop()
            self.visit(currV)
            self.enqueue(queue,currV.adjList,seen)
    #
    def visit(self,vertex):
        """default implementation of \"visit a vertex.\""""
        print(vertex.vtx)
    #
    def enqueue(self, fifoQ, adjList, seenDict):
        """default implementation of \"handle the adjacency list of a vertex.\""""
        for locVertex in adjList:
            if seenDict.get(locVertex.vtx) is None:
                seenDict[locVertex.vtx]=True
                fifoQ.append(locVertex.vtx)
                
