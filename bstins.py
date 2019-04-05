# Should a binary-search-tree be a reference to a
# network of interconnected BSTNode's?
# And how does that change the shape of the 
# insertion process/function?

class BSTree:
    def __init__(self, node):
        self._root = node

    def insert(self, v):
        if self._root is None:
            self._root = BSTNode(v, None, None)
        else:
            self._insert(self._root, v)

    def _insert(self, t, v):
        if (t.key() < v):
            if (t.rChild() is None):
                t._rChild = BSTNode(v, None, None)
            else:
                self._insert(t.rChild(),v)
        else:
            if(t.lChild() is None):
                t._lChild = BSTNode(v, None, None)
            else:
                self._insert(t.lChild(),v)
    #
    def buildTree(self, values):
        for v in values:
            self.insert(v)
    #
    def inorderPrint(self):
        if self._root is None:
            return
        self._inorderPrint(self._root)
        
    def _inorderPrint(self, treeRoot):
        if treeRoot is None:
            return  # i.e., there's nothing to print!
        #
        self._inorderPrint(treeRoot.lChild())
        print ("value: ", treeRoot.key())
        self._inorderPrint(treeRoot.rChild())

    def bstDistance(self, v1, v2):
        if v2 < v1:
            v1, v2 = v2, v1  # swap them!
        #
        treeRoot = self._root
        #
        if treeRoot is None:
            return 0  # what is the distance when the tree is "empty?"
        #
        distance = 0
        #
        while v2 < treeRoot.key() or treeRoot.key() < v1:
            if v2 < treeRoot.key():
                treeRoot = treeRoot.lChild()
            else:
                treeRoot = treeRoot.rChild()
        #
        # Now, treeRoot.key() <= v2 and v1 <= treeRoot.key()
        # Assuming that v1 != v2, then:
        # we must calculate the path length from treeRoot down to v1
        # and then calculate the path length from treeRoot down to v2:
        return self._pathFromRoot(treeRoot, v1) + self._pathFromRoot(treeRoot, v2)

    def _pathFromRoot(self, treeRoot, v):
        dist = 0
        #
        while treeRoot is not None and treeRoot.key() != v:
            if treeRoot.key() < v:
                treeRoot = treeRoot.rChild()
            else:
                treeRoot = treeRoot.lChild()
            #
            dist = dist + 1
        #
        return dist

class BSTNode:
    def __init__(self, data, lChild, rChild):
        self._data = data
        self._lChild = lChild
        self._rChild = rChild

    def lChild(self):
        return self._lChild

    def rChild(self):
        return self._rChild

    def key(self):
        return self._data


if __name__ == "__main__":
    myT = BSTree(BSTNode(1,None,None))
    #
    myT.insert(9)
    #
    myT.inorderPrint()
    #
    print (myT.bstDistance(1, 9))
    #
    myT2 = BSTree(None)
    myT2.buildTree([10,9,8,5,6,7,3,4,2,1])
    myT2.inorderPrint()
    print (myT2.bstDistance(7,8) == 3)

    myT3=BSTree(None)
    myT3.buildTree([1,8,9,10,5,6,7,3,4,2])
    print (myT3.bstDistance(4,7) == 4)
    
