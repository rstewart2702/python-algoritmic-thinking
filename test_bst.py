import unittest
import bst


"""
This is an example of how unit testing could be used with the 
BSTree class.

The unit tests herein use the standard unittest module provided
by Python 3.x and higher.

This can be run from the command line with something like:
  python -m unittest test_bst
"""

class testBSTDistanceT1(unittest.TestCase):
    def setUp(self):
        self.myT = bst.BSTree(bst.BSTNode(1,None,None))
        self.myT.insert(9)

    def testDistanceT1(self):
        self.assertEqual(1,self.myT.bstDistance(1,9))


class testBSTDistanceT2(unittest.TestCase):
    def setUp(self):
        # confirmed:
        #   the "driving" program/class sends the setUp message
        #   before it sends one of the "test" messages.
        # AND
        #   for each "test" message-send, the setUp message is sent first
        print("\nExecuting testBSTDistanceT2.setUp!")
        self.myT2 = bst.BSTree(None)
        self.myT2.buildTree([10,9,8,5,6,7,3,4,2,1])
        #
        self.myT3 = bst.BSTree(None)
        self.myT3.buildTree([1,8,9,10,5,6,7,3,4,2])

    def testDistanceT2(self):
        self.assertEqual(3,self.myT2.bstDistance(7,8))

    def testDistanceT3(self):
        self.assertEqual(4,self.myT3.bstDistance(4,7))
