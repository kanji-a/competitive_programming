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

def resolve():
    N, M = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, C = LI()
        A -= 1
        B -= 1
        G[A].append((B, C))

    for i in range(N):
        que = []
        dist = [INF] * N
        for j, d in G[i]:
            heapq.heappush(que, (d, j))
            dist[j] = min(d, dist[j])
        while que:
            d, c = heapq.heappop(que)
            if dist[c] < d:
                continue
            for n in G[c]:
                if dist[n[0]] > dist[c] + n[1]:
                    dist[n[0]] = dist[c] + n[1]
                    heapq.heappush(que, (dist[n[0]], n[0]))
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])

if __name__ == '__main__':
    resolve()
