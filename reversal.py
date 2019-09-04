def reversal(a):
    b = a.copy()
    N = len(a)
    #
    for i in range(N // 2):
        print(a[0:i], a[i:N-i], a[N-i:N], sep=' : ')
        print(b[0:i], b[i:N-i], b[N-i:N], sep=' : ')
        print(a[0:i]==revcopy(b[N-i:N]))
        print(a[N-i:N]==revcopy(b[0:i]))
        print(a[i:N-i]==b[i:N-i])
        #
        a[i],a[N-1-i] = a[N-1-i],a[i]
        #
        print('\n')
    #
    M = N//2
    print(a[0:M], a[M:N-M], a[N-M:N], sep=' : ')
    print(b[0:M], b[M:N-M], b[N-M:N], sep=' : ')
    print(a[0:M]==revcopy(b[N-M:N]))
    print(a[N-M:N]==revcopy(b[0:M]))
    print(a[M:N-M]==b[M:N-M])

def revcopy(a):
    r = a.copy()
    r.reverse()
    return r
