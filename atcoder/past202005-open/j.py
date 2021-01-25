import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    a = LI()

    # 最後に食べた寿司の美味しさは単調減少になるので二分探索
    d = [0] * N
    for i in a:
        ng = -1
        ok = N
        while abs(ok - ng) > 1:
            m = (ng + ok) // 2
            if d[m] < i:
                ok = m
            else:
                ng = m
        if ok == N:
            print(-1)
        else:
            print(ok + 1)
            d[ok] = i

if __name__ == '__main__':
    resolve()
