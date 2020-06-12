N, Q = map(int, input().split())
PAB = [list(map(int, input().split())) for _ in range(Q)]

par = list(range(N))

def root(x):
    if(par[x] == x):
        return x
    else:
        par[x] = root(par[x])
        return par[x]

for i in range(Q):
    A = PAB[i][1]
    B = PAB[i][2]
    if PAB[i][0] == 0:
        rA = root(A-1)
        rB = root(B-1)
        if (rA != rB):
            par[rA] = rB
    else:
        if root(A-1) == root(B-1):
            print('Yes')
        else:
            print('No')