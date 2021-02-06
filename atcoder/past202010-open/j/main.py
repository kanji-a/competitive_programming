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

def resolve():
    N, M = LI()
    X = LI()
    # X = [[INF, X[0], X[1]], [X[0], INF, X[2]], [X[1], X[2], INF]]
    S = SS()
    # S = [ord(i) - ord('A') for i in SS()]
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, C = LI()
        G[A-1].append((B - 1, C))
        G[B-1].append((A - 1, C))
    # ワープ台X→ワープ台Yを
    # ワープ台X→町X_in→町Y_out→ワープ台Yと考えればよい
    A_in = N
    A_out = N + 1
    B_in = N + 2
    B_out = N + 3
    C_in = N + 4
    C_out = N + 5
    G[A_in].append((B_out, X[0]))
    G[B_in].append((A_out, X[0]))
    G[A_in].append((C_out, X[1]))
    G[C_in].append((A_out, X[1]))
    G[B_in].append((C_out, X[2]))
    G[C_in].append((B_out, X[2]))
    for i, e in enumerate(S):
        if e == 'A':
            G[i].append((A_in, 0))
            G[A_out].append((i, 0))
        elif e == 'B':
            G[i].append((B_in, 0))
            G[B_out].append((i, 0))
        else:
            G[i].append((C_in, 0))
            G[C_out].append((i, 0))
    # print(G)

    ans = dijkstra(G, N + 6, 0)[N-1]

    print(ans)

if __name__ == '__main__':
    resolve()

