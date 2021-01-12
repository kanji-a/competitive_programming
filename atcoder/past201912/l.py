import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
from atcoder.dsu import DSU
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    dsu = DSU(V)
    res = 0
    for e in es:
        if not dsu.same(e[0], e[1]):
            dsu.merge(e[0], e[1])
            res += e[2]
    return res

def resolve():
    N, M = LI()
    E = []
    xyc = [LI() for _ in range(N)]
    for i, j in itertools.combinations(range(N), 2):
        x0, y0, c0 = xyc[i]
        x1, y1, c1 = xyc[j]
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        if c0 != c1:
            d *= 10
        E.append((i, j, d))
    XYC = [LI() for _ in range(M)]

    # 全ての小さい塔の組み合わせに対してBIT全探索してMST
    ans = INF
    for i in range(2 ** M):
        EE = copy.deepcopy(E)
        # 小さい塔同士の辺
        for j, k in itertools.combinations(range(M), 2):
            if i >> j & 1 and i >> k & 1:
                X0, Y0, C0 = XYC[j]
                X1, Y1, C1 = XYC[k]
                d = ((X1 - X0) ** 2 + (Y1 - Y0) ** 2) ** 0.5
                if C0 != C1:
                    d *= 10
                EE.append((N + j, N + k, d))
        # 小さい塔から大きい塔への辺
        for j in range(M):
            if i >> j & 1:
                X, Y, C = XYC[j]
                for k in range(N):
                    x, y, c = xyc[k]
                    d = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
                    if C != c:
                        d *= 10
                    EE.append((N + j, k, d))
        ans = min(kruskal(EE, N + M), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
