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
    AB = [LI_() for _ in range(M)]
    AB.sort()
    deg = [0] * N
    G = collections.defaultdict(list)
    for A, B in AB:
        G[A].append(B)
        deg[B] += 1

    ans = []
    hq = []
    for i in range(N):
        if deg[i] == 0:
            heapq.heappush(hq, i)
    while hq:
        c = heapq.heappop(hq)
        ans.append(c + 1)
        for n in G[c]:
            deg[n] -= 1
            if deg[n] == 0:
                heapq.heappush(hq, n)

    if len(ans) == N:
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
