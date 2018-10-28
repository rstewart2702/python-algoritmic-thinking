
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
    curr = 0
    stk = [curr]
    hop = 0
    while (t[curr]["key"] != node1):
        if (node1 <= t[curr]["key"]):
            stk.append(t[curr]["r"])
            curr = t[curr]["r"]
        else:
            stk.append(t[curr]["l"])
            curr = t[curr]["l"]
    #
    while (t[curr]["key"] != node2):
        if (t[curr]["key"] < node2):
            if (search(t,t[curr]["r"],node2)):
                hop = hop + 1
                curr = t[curr]["r"]
            elif (search(t,t[curr]["l"],node2)):
                hop = hop + 1
                curr = t[curr]["l"]
            else:
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
