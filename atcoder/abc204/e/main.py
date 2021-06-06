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

def dijkstra(G, N, s):
    que = []
    d = [INF] * N
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))
    return d

def resolve():
    N, M = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, C, D = LI()
        A -= 1
        B -= 1
        G[A].append((B, C, D))

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
            t0 = max(int(D ** 0.5) - 1, 0)
            t1 = int(D ** 0.5)
            next_time0 = t0 + e[1] + e[2] // (t0 + 1)
            next_time1 = t1 + e[1] + e[2] // (t1 + 1)
            t = -1
            if next_time0 < next_time1:
                t = t0
            else:
                t = t1
            t = max(d[v], t)
            if d[e[0]] > t + e[1] + e[2] // (t + 1):
                d[e[0]] = t + e[1] + e[2] // (t + 1)
                heapq.heappush(que, (d[e[0]], e[0]))
    # print(d)

    if d[-1] == INF:
        print(-1)
    else:
        print(d[-1])

if __name__ == '__main__':
    resolve()
