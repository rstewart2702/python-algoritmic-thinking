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
        rep1v = self.find(v1).vtx
        rep2v = self.find(v2).vtx
        self.sets[rep2v].parent = rep1v
    #
    def union1(self, v1, v2):
        """This version of the \"union\" operation doesn't do enough!  It does
not perform needed path-traversal to get to the ultimate parent of either
of the vertices in question.
The test output should prove this out."""
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
        # print('Found ',curV.vtx, ' in ',find_hops,' hops')
        return curV
    
if __name__ == '__main__':
    vList = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11']
    x = DisjointSets(vList)
    #
    x.union('v5','v6')
    x.union('v9','v8')
    x.union('v11','v10')
    print([ x.find(itm).vtx for itm in vList] )
    x.union('v9','v10')
    print([ x.find(itm).vtx for itm in vList] )
    print(x.find('v8').vtx)
    print([ x.find(itm).vtx for itm in vList ] )
    print()
    #
    y = DisjointSets(vList)
    y.union1('v5','v6')
    y.union1('v9','v8')
    y.union1('v11','v10')
    print('Representative of v10 is: ',y.find('v10').vtx)
    print([ y.find(itm).vtx for itm in vList] )
    y.union1('v9','v10')
    print('Representative of v11 is: ',y.find('v11').vtx)
    print('Representative of v10 is: ',y.find('v10').vtx)
    print([ y.find(itm).vtx for itm in vList] )
    #
    print(y.find('v8').vtx)
    print([ y.find(itm).vtx for itm in vList] )
