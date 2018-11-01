
def insert(t,ptr,v):
    if (t[ptr]['key'] < v):
        if (t[ptr]['r'] == -1):
            t.append({'key': v, 'l': -1, 'r': -1})
            t[ptr]['r'] = len(t)-1
        else:
            insert1(t,t[ptr]['r'],v)
    else:
        if (t[ptr]['l'] == -1):
            t.append({'key': v, 'l': -1, 'r': -1})
            t[ptr]['l'] = len(t)-1
        else:
            insert1(t,t[ptr]['l'],v)

def search(t,ptr,v):
    if (ptr == -1):
        return False
    if (t[ptr]["key"] == v):
        return True
    if (t[ptr]["key"] < v):
        return search(t,t[ptr]["r"],v)
    else:
        return search(t,t[ptr]["l"],v)

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
    curr, stk, hop, dca = 0, [], 0, 0
    while (    not(node1 < t[curr]['key'] and t[curr]['key'] < node2)
           and node1 != t[curr]['key']
           and node2 != t[curr]['key']):
        stk.append(curr)
        if (t[curr]['key'] < node1):
            curr = t[curr]['r']
        else:
            curr = t[curr]['l']
    #
    # so now:
    #     t[curr]['key'] < node1 and t[curr]['key'] < node2
    #  or node1 == t[curr]['key']
    #  or node2 == t[curr]['key']
    # and so we should store curr into dca, no?
    dca = curr
    print ("Deepest common ancestor is", t[dca]['key'])
    #
    # Now we must continue the search down to node1:
    while(t[curr]['key'] != node1):
        stk.append(curr)
        if (t[curr]['key'] < node1):
            curr = t[curr]['r']
        else:
            curr = t[curr]['l']
    #
    # Now t[curr]['key'] == node1.
    # Now we traverse back up to the "deepest-common-ancestor," dca,
    # from which we may need to traverse "downwards" in order to search for node2:
    while(curr != dca):
        curr = stk.pop()
        hop = hop + 1
    #
    # Now curr == dca.
    while (t[curr]['key'] != node2):
        hop = hop + 1
        if (t[curr]['key'] < node2):
            curr = t[curr]['r']
        else:
            curr = t[curr]['l']
    #
    return hop


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

