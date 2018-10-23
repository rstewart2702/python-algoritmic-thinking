myarr = [10,-1,10,-2,-20]
myarr2 = [10,-1,10,-2,-8]

a3 = [10, -1, 5, -11, 8, 6, -21, -2, 15, -1, 16, -4, 8, 16]
a4 = [10, -1, 5, -11, 8, 6, -21, -2, 15, -1, 16, -4, 8, 16, -2]

a5 = [1, 2, -6, 9, 16, -10, 46, -30, 42, 18, -6, -9, -7, 14, 92]

a6 = [1500, 1, 2, -6, 9, 16, -10, 46, -30, 42, 18, -6, -9, -7, 14, 92]

a7 = [1500, 1, 2, -6, 9, 16, -10, 46, -30, 42, 18, -6, -9, -7, 14, 92, -2000]


a8 = [-1, 10, -1, 5, -11, 8, 6, -21, -2, 15, -1, 16, -4, 8, 16, -2]

a9 = [-1, 10, -1, 5, -11, 8, 6, -21, -2, 15, -1, 16, -4, 8, 16, -2, -14]

def inner(a, t, N):
    i,j,s,sp,jp = t,t+1,a[t],0,t-1
    #
    while (0 < s and s+a[j] > 0):
        if (a[j] <= 0):
            s,j = s+a[j],j+1
        elif (a[j] > 0):
            s,sp,j,jp = s+a[j],s+a[j],j+1,j
    #
    return (a, a[i:jp+1], a[i:j+1], j, jp, s, sp)

# This is pretty close to, or is exactly, what is needed
# in an "inner iteration" of some kind of "find the greatest subsequence sum"
# solution.
#   jp ::=
#     i <= jp < j  and  a[jp] > 0 and all(u : jp < u <= j : a[u] <= 0)
#     or
#     jp < i
#
#   s  ::= sum(x, i <= x <   j : a[x])
#
#   sp ::= sum(x, i <= x <= jp : a[x])
#
#   t <= i < j < t+N
#
# This is almost what one would write in Dijkstra's guarded command language!
def inner2(a, t, N):
    i,j,s,sp,jp = t,t+1,a[t],0,t-1
    #
    while (j < N and 0 < s and 0 < s+a[j]):
        if (a[j] <= 0):
            s,j = s+a[j],j+1
        elif (0 < a[j]):
            s,sp,j,jp = s+a[j],s+a[j],j+1,j
    #
    # upon exit from the loop:
    #   j = N   i.e., we've run out of array
    #   or
    #   s <= 0  the most recently added element was large enough negative to make the sum "go negative"
    #   or
    #   s + a[j] <= 0 the next element which could be added will cause the sum to be negative
    #
    return (a, a[i:jp+1], a[i:j+1], j, jp, s, sp)


if __name__ == "__main__":
    print (inner2(a3, 0, len(a3)))
    print (inner2(a3, 8, len(a3)))
    print (inner2(a4, 8, len(a4)))
    #
    print ("\n")
    print (inner2(a9, 1, len(a9)))
    print (inner2(a9, 9, len(a9)))
