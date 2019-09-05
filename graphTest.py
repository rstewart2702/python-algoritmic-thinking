import unittest

import graph
from graph import Graph as Graph, Vertex as Vertex

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
                        
