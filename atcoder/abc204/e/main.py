#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, C, D = LI()
        A -= 1
        B -= 1
        G[A].append((B, C, D))
        G[B].append((A, C, D))

    que = []
    d = [INF] * N
    s = 0
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            # 移動時間が最小になる時刻
            sqrtD = int(e[2] ** 0.5)
            tmp = d[v] + e[1] + e[2] // (d[v] + 1)
            for t in range(max(sqrtD - 5, d[v]), sqrtD + 6):
                tmp = min(t + e[1] + e[2] // (t + 1), tmp)
            if d[e[0]] > tmp:
                d[e[0]] = tmp
                heapq.heappush(que, (d[e[0]], e[0]))
    # print(d)

    if d[-1] == INF:
        print(-1)
    else:
        print(d[-1])

if __name__ == '__main__':
    resolve()
