class BSTNode:
    def BSTNode(self, data, lChild, rChild):
        self._data = data
        self._lChild = lChild
        self._rChild = rChild

    def lChild(self):
        return self.lChild

    def rChild(self):
        return self.rChild

    

    
def insert(t,ptr,v):
    if (t[ptr]['key'] < v):
        if (t[ptr]['r'] == -1):
            t.append({'key': v, 'l': -1, 'r': -1})
            t[ptr]['r'] = len(t)-1
        else:
            insert(t,t[ptr]['r'],v)
    else:
        if (t[ptr]['l'] == -1):
            t.append({'key': v, 'l': -1, 'r': -1})
            t[ptr]['l'] = len(t)-1
        else:
            insert(t,t[ptr]['l'],v)

def search(t,ptr,v):
    if (ptr == -1):
        return False
    if (t[ptr]["key"] == v):
        return True
    if (t[ptr]["key"] < v):
        return search(t,t[ptr]["r"],v)
    else:
        return search(t,t[ptr]["l"],v)

def downTo(t,curr,node):
    hop = 0
    while (t[curr]['key'] != node):
        if (t[curr]['key'] < node):
            hop, curr = hop+1, t[curr]['r']
        else:
            hop, curr = hop+1, t[curr]['l']
    return hop
        

def distShell(t,node1,node2):
    # swap the ordering of node1 and node2, just to guarantee
    # that node1 < node2:
    if (node2 < node1):
        tmp=node2
        node2=node1
        node1=tmp
    #
    # Traverse down to node1, looking for the "lowest-in-the-tree" common
    # vertex on both paths from node1 to node2.
    # This common-vertex will be the place to which the algorithm
    # ascends after finding node1, in order to compute the distance from node1 to node2.
    curr = 0
    # N.B. node1 < node2,
    # AND
    # the expression:
    #       t[curr]['key'] != node1 and t[curr]['key'] != node2
    #   and not(node1 < t[curr]['key'] and t[curr]['key'] < node2)
    # simplifies to:
    #   node2 < t[curr]['key'] or t[curr]['key'] < node1
    # which is the loop guard used here.
    while (t[curr]['key'] < node1 or node2 < t[curr]['key']):
        # i.e., while both node1 and node2 lie to the right of the current node
        #          or both node1 and node2 lie to the left of the current node
        # then we haven't found the "deepest common ancestor" yet.
        if (t[curr]['key'] < node1):
            curr = t[curr]['r']
        else:
            curr = t[curr]['l']
    #
    # so now:
    #     node1 < t[curr]['key'] and t[curr]['key'] < node2
    #  or node1 == t[curr]['key']
    #  or node2 == t[curr]['key']
    # and so we should store curr into dca, no?
    print ("Deepest common ancestor is", t[curr]['key'])
    #
    return downTo(t,curr,node1) + downTo(t,curr,node2)

def buildTree(values):
    r = {"key": values[0], "l" : -1, "r": -1 }
    tree = [r]
    #
    for v in values[1:]:
        insert(tree,0,v)
    return tree

def bstDistance(values, n, node1, node2): 
    # create root node:
    if (n == 0):
        return -1
    #
    tree = buildTree(values)
    # 
    #
    return distShell(tree,node1,node2)

if __name__ == "__main__":
    print bstDistance([10,9,8,5,6,7,3,4,2,1],10,7,8) == 3
    print bstDistance([10,9,8,5,6,7,3,4,2,1],10,1,7) == 5
    print bstDistance([1,8,9,10,5,6,7,3,4,2],10,7,8) == 3
    print bstDistance([1,8,9,10,5,6,7,3,4,2],10,4,7) == 4
    #
    print bstDistance([8,48,32,46,2,1,5,3],8,2,3) == 2
    print bstDistance([8,48,32,46,2,1,5,3],8,3,48) == 4
    #
    print bstDistance([8,2,48,1,5,32,46,3],7,3,1) == 3
    print bstDistance([8,2,48,1,5,32,46,3],7,32,48) == 1
    print bstDistance([8,2,48,1,5,32,46,3],7,32,8) == 2
    print bstDistance([8,2,48,1,5,32,46,3],7,3,32) == 5
    

