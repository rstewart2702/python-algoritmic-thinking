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
        rep1 = self.find(v1)
        rep2 = self.find(v2)
        self.sets[v2].parent = v1
    #
    def find(self, vtx):
        """Return the ultimate, representing-member of the subset that contains
the vertex named by vtx."""
        find_hops=0
        curV = self.sets[vtx]
        while(curV.parent is not None):
            curV = self.sets[curV.parent]
            find_hops = find_hops+1
        #
        print('Found ',curV.vtx, ' in ',find_hops,' hops')
        return curV
    
if __name__ == '__main__':
    vList = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11']
    x = DisjointSets(vList)
    #
    x.union('v5','v6')
    x.union('v9','v8')
    x.union('v11','v10')
    x.union('v9','v10')
    print(x.find('v8').vtx)
    print([ x.find(itm).vtx for itm in vList ] )

    
