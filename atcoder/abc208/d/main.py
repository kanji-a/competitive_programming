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
    d = [[INF] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for _ in range(M):
        A, B, C = LI()
        A -= 1
        B -= 1
        d[A][B] = C

    ans = 0
    for k in range(N):
        nxt = [[0] * N for _ in range(N)]
        for s in range(N):
            for t in range(N):
                nxt[s][t] = min(d[s][t], d[s][k] + d[k][t])
                if nxt[s][t] < INF:
                    ans += nxt[s][t]
        d = nxt

    print(ans)

if __name__ == '__main__':
    resolve()
