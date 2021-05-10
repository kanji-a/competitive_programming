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
    N, B, K = LI()
    c = LI()

    dp = [[0] * B for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(B):
            for k in c:
                dp[i+1][(j*10+k)%B] += dp[i][j]
                dp[i+1][(j*10+k)%B] %= MOD
    # for i in dp:
    #     print(i)

    print(dp[-1][0])

if __name__ == '__main__':
    resolve()
