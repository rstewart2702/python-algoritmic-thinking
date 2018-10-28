
def insert(t,ptr,v):
    # recursive insert into tree t
    #
    if (t[ptr]["key"] < v):
        if (t[ptr]["r"] == -1):
            t.append({"key": v, "l": -1, "r": -1})
            t[ptr]["r"] = len(t)-1
        else:
            insert(t,t[ptr]["r"],v)
        #
    else:
        if (t[ptr]["l"] == -1):
            t.append({"key": v, "l": -1, "r": -1})
            t[ptr]["l"] = len(t)-1
        else:
            insert(t,t[ptr]["r"],v)
            
    #

def insertR(t,ptr,v):
    if (ptr == -1):
        t.append({'key': v, 'l':-1, 'r':-1})
        
    #
    if (t[ptr]['key'] < v):
        t[ptr]['r'] = insertR(t,t[ptr]['r'],v)
    else:
        t[ptr]['r'] = insertR(t,t[ptr]['l'],v)

def insert1(t,ptr,v):
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
    

def distShell(t,node1, node2):
    # swap the ordering of node1 and node2, just to guarantee
    # that node1 < node2:
    if (node2 < node1):
        tmp=node2
        node2=node1
        node1=tmp
    #
    curr = 0
    stk = []
    hop = 0
    while (t[curr]["key"] != node1):
        stk.append(curr)
        if (t[curr]['key'] <= node1):
            curr = t[curr]["r"]
        else:
            curr = t[curr]["l"]
    #
    print ("found ",node1,", now searching for ",node2,":")
    while (t[curr]["key"] != node2):
        # it might be more "honest" to simply increase hop-count
        # when traversing "down" into a subtree, and then subtracting
        # hops when you must return from a subtree because you couldn't
        # find the node2...
        # There's another possible optimization:
        #   if node2 falls between current and parent,
        #   then we may hop up to parent,
        #        and then drop down to the right-hand child,
        #        counting hops all the way downwards.
        #   otherwise, we pop up to the parent, adding one to the hop count.
        parent = stk[len(stk)-1]
        if (t[curr]['key'] < node2 and node2 <= t[parent]['key']):
            hop = hop + 2 # up to parent, down to right child of parent
            curr = stk.pop()
            curr = t[t[curr]['r']]['l']
            ### AND NOW WE NEED A LOOP TO TRAVERSE BACK DOWN TO node2,
            ### WHICH IS GUARANTEED TO RESIDE IN TREE ROOTED AT
            ### t[curr].
        else:
            hop = hop + 1
            curr = stk.pop()
        ##
        if (search(t,t[curr]["r"],node2)):
            print (node2," is to right of ",t[curr]['key'])
            hop = hop + 1
            curr = t[curr]["r"]
        elif (search(t,t[curr]["l"],node2)):
            print (node2, "is to the left of ",t[curr]['key'])
            hop = hop + 1
            curr = t[curr]["l"]
        else:
            print (node2, "must be found via parent of ",t[curr]['key']," which is :",t[stk[len(stk)-1]]['key'])
            hop = hop + 1
            curr = stk.pop()
    #
    return hop

def buildTree(values):
    r = {"key": values[0], "l" : -1, "r": -1 }
    tree = [r]
    #
    for v in values[1:]:
        insert1(tree,0,v)
    return tree

def bstDistance(values, n, node1, node2): 
    # create root node:
    if (n == 0):
        return -1
    #
    r = {"key": values[0], "l" : -1, "r": -1 }
    tree = [r]
    curr = tree[0]
    # 
    for v in values[1:]:
        insert(tree,0,v)
    #
    return distShell(tree,node1,node2)
