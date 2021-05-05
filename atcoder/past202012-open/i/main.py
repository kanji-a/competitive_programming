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
    N, M, K = LI()
    H = LI()
    C = set(LI_())
    G = collections.defaultdict((list))
    for _ in range(M):
        A, B = LI_()
        if H[A] > H[B]:
            G[A].append(B)
        else:
            G[B].append(A)

    dp = [INF] * N
    for i, _ in sorted(enumerate(H), key=lambda x: x[1]):
        if i in C:
            dp[i] = 0
            continue
        tmp = INF
        for n in G[i]:
            tmp = min(dp[n], tmp) 
        dp[i] = tmp + 1
    # print(dp)

    for i in dp:
        if i == INF:
            print(-1)
        else:
            print(i)

if __name__ == '__main__':
    resolve()
