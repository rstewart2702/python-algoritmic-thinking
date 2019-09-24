# union-find, disjoin-set implementation?
from graph import Vertex as Vertex, Graph as Graph, GraphPaths as GraphPaths

class UFNode:
    def __init__(self, vtx):
        self.vtx = vtx
        self.parent = None
    #

class DisjointSets:
    def __init__(self, vertices):
        self.sets = {}
        for v in vertices:
            self.sets[v] = UFNode(v)
    #
    def union(self, v1, v2):
        self.sets[v2].parent = v1
    #
#     def find(self, vtx):
        
