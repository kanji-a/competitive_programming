#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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

# x以上の最小のkの倍数
def f(x, k):
    return ((x - 1) // k + 1) * k

def resolve():
    N, M, X, Y = LI()
    X -= 1
    Y -= 1
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, T, K = LI()
        A -= 1
        B -= 1
        G[A].append((B, T, K))
        G[B].append((A, T, K))

    que = []
    d = [INF] * N
    d[X] = 0
    heapq.heappush(que, (d[X], X))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e[0]] > f(d[v], e[2]) + e[1]:
                d[e[0]] = f(d[v], e[2]) + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))

    if d[Y] == INF:
        print(-1)
    else:
        print(d[Y])

if __name__ == '__main__':
    resolve()
