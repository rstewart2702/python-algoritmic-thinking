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
        seen = {startVtx : True}  # set of seen vertices, as a dictionary
        visited = [] # start out with an empty "visited list"
        # append to back, pop off front
        while(len(queue) != 0):
            currV = queue.pop(0)
            self.visit(currV,visited)
            self.enqueue(queue,self.nodes[currV].adjList,seen)
            #
            # print(currV,visited,queue,seen,sep='::')
            # print('\n')
        #
        return visited
    #
    def visit(self,vertex,visited):
        """default implementation of \"visit a vertex.\""""
        visited.append(vertex)
    #
    def enqueue(self, fifoQ, adjList, seenDict):
        """default implementation of \"handle the adjacency list of a vertex.\""""
        for locVertex in adjList:
            if seenDict.get(locVertex) is None:
                seenDict[locVertex]=True
                fifoQ.append(locVertex)
                

class GraphPaths(Graph):
    """Derived from class Graph.
The methods bfs and enqueue are overridden since the behavior is different...
"""
    def bfs(self, startVtx):
        currV = None
        queue = [startVtx]
        seen = {startVtx : True}
        visited = []
        paths = {startVtx : [] }
        for v in self.nodes[startVtx].adjList:
            paths[v] = [v]
        #
        while(len(queue) != 0):
            currV = queue.pop(0)
            self.visit(currV,visited)
            self.enqueue(queue,self.nodes[currV].adjList,seen,paths,currV)
        #
        return (visited, paths)
    #
    def enqueue(self, fifoQ, adjList, seenDict, paths,currV):
        # print('before enqueue:',paths,sep=' ')
        for locVertex in adjList:
            if seenDict.get(locVertex) is None:
                seenDict[locVertex]=True
                fifoQ.append(locVertex)
                paths[locVertex]=paths[currV].copy()
                paths[locVertex].append(locVertex)
                # paths[locVertex]=[locVertex]
            else:
                # The adjacent vertex has been seen before.
                #
                print('Evaluating:',paths[locVertex])
                print('against:',paths[currV])
                currLen = len(paths[locVertex])
                newLen = len(paths[currV])+1
                if newLen < currLen:
                    # if the length of the "newer path" is shorter
                    # then it should replace the existing path
                    print('Replacing path:',paths[locVertex])
                    paths[locVertex] = paths[currV].copy()
                    paths[locVertex].append(locVertex)
                    print('With path:',paths[locVertex])
        # print('after enqueue:',paths,sep=' ')

                
