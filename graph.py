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
