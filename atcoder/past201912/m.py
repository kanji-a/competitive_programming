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
    N, M = LI()
    AB = [LI() for _ in range(N)]
    CD = [LI() for _ in range(M)]

    # 決め打ち二分探索
    # ΣB/ΣA≧X ⇔ Σ(B-XA)≧0

    def is_ok(X):
        AB_ = [b - X * a for a, b in AB]
        CD_ = [d - X * c for c, d in CD]
        sorted_AB = sorted(AB_, reverse=True)
        res = sum(sorted_AB[:5]) >= 0 or sum(sorted_AB[:4]) + max(CD_) >= 0
        return res

    ng = 10 ** 9
    ok = 0
    while abs(ok - ng) > 10e-7:
        m = (ng + ok) / 2
        if is_ok(m):
            ok = m
        else:
            ng = m

    print(m)

if __name__ == '__main__':
    resolve()
