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
    W, N = LI()
    LRV = [LI() for _ in range(N)]

    dp = [-1] * (W + 1)
    for i in range(N):
        dp[0] = 0

    for i in range(N):
        L, R, V = LRV[i]
        for j in range(W, 0, -1):
            tmp = -1
            for k in range(L, R + 1):
                if 0 <= j - k and dp[j-k] >= 0:
                    tmp = max(dp[j-k] + V, tmp)
            # セグ木で区間maxを求める
            if dp[j] >= 0:
                tmp = max(dp[j], tmp)
            dp[j] = tmp

    print(dp[-1])

if __name__ == '__main__':
    resolve()
