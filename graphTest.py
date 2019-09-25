import unittest

from graph import Graph as Graph, \
     Vertex as Vertex, \
     GraphPaths as GraphPaths # , \
#      GraphWPaths as GraphWPaths

class testGraphBfs1(unittest.TestCase):
    def setUp(self):
        self.gLocal = \
                    Graph.gBuild( [
                        Vertex.newV('v1').adjAdd(['v2','v3','v8']),
                        Vertex.newV('v2').adjAdd(['v1','v8']),
                        Vertex.newV('v3').adjAdd(['v1','v8']),
                        Vertex.newV('v4').adjAdd(['v8']),
                        Vertex.newV('v5').adjAdd(['v6','v7']),
                        Vertex.newV('v6').adjAdd(['v5','v7','v11']),
                        Vertex.newV('v7').adjAdd(['v5','v6','v8']),
                        Vertex.newV('v8').adjAdd(['v1','v2','v3','v4','v7','v10']),
                        Vertex.newV('v9').adjAdd(['v10','v11']),
                        Vertex.newV('v10').adjAdd(['v8','v9','v11']),
                        Vertex.newV('v11').adjAdd(['v6','v9','v10'])
                        ] )

    def testBfs1(self):
        self.assertEqual(
            ['v1','v2','v3','v8','v4','v7','v10','v5','v6','v9','v11'],
            self.gLocal.bfs('v1')
            )
                        
class testGraphBfsPaths(unittest.TestCase):
    def setUp(self):
        self.gLoc1 = \
                   GraphPaths.gBuild( [
                        Vertex.newV('v1').adjAdd(['v2','v3','v4','v8']),
                        Vertex.newV('v2').adjAdd(['v1','v8']),
                        Vertex.newV('v3').adjAdd(['v1','v8']),
                        Vertex.newV('v4').adjAdd(['v1','v5','v8']),
                        Vertex.newV('v5').adjAdd(['v4','v6','v7','v12']),
                        Vertex.newV('v6').adjAdd(['v5','v7','v11','v12']),
                        Vertex.newV('v7').adjAdd(['v5','v6','v8']),
                        Vertex.newV('v8').adjAdd(['v1','v2','v3','v4','v7','v10','v12']),
                        Vertex.newV('v9').adjAdd(['v10','v11']),
                        Vertex.newV('v10').adjAdd(['v8','v9','v11','v12']),
                        Vertex.newV('v11').adjAdd(['v6','v9','v10']),
			Vertex.newV('v12').adjAdd(['v5','v10','v6','v8'])
                        ] )

    def testBfsPaths1(self):
        self.assertEqual(
            (['v3', 'v1', 'v8', 'v2', 'v4', 'v7', 'v10', 'v12', 'v5', 'v6', 'v9', 'v11'], \
             {'v3': [],
              'v1': ['v1'],
              'v8': ['v8'],
              'v2': ['v1', 'v2'],
              'v4': ['v1', 'v4'],
              'v7': ['v8', 'v7'],
              'v10': ['v8', 'v10'],
              'v12': ['v8', 'v12'],
              'v5': ['v1', 'v4', 'v5'],
              'v6': ['v8', 'v7', 'v6'],
              'v9': ['v8', 'v10', 'v9'],
              'v11': ['v8', 'v10', 'v11']}),
            self.gLoc1.bfs('v3')
            )

class testGraphBfsWPaths(unittest.TestCase):
    """Tests for weighted simple graphs, to test the \"Dijkstra all-points-shortest-paths\" computation."""
    def setUp(self):
        self.gLoc1 = \
                   GraphWPaths.gBuild( [
                       Vertex.newV('v1').adjAdd([('v4',2),('v2',3),('v3',10),('v8',9)])
                       ] )
