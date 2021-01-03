import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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

def resolve():
    N = I()
    G = collections.defaultdict(list)
    ab = [LI_() for _ in range(N - 1)]
    # print(ab)
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)
    par = [-1] * N
    def rec(c, p):
        par[c] = p
        for n in G[c]:
            if n != p:
                rec(n, c)
    rec(0, -1) 
    # print(par)

    # 木上のimos法
    ans = [0] * N
    imos = [0] * N
    Q = I()
    for _ in range(Q):
        t, e, x = LI()
        e -= 1
        a, b = ab[e]
        # 親方向
        if t == 1:
            # 親方向
            if a == par[b]:
                imos[0] += x
                imos[b] -= x
            # 子方向
            else:
                imos[a] += x
        else:
            # 親方向
            if b == par[a]:
                imos[0] += x
                imos[a] -= x
            # 子方向
            else:
                imos[b] += x
        # print(imos)
    
    def rec1(cur, p):
        if p == -1:
            ans[cur] = imos[cur]
        else:
            ans[cur] = ans[p] + imos[cur]
        for n in G[cur]:
            if n != p:
                rec1(n, cur)
    rec1(0, -1) 

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
