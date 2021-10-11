#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    a = LI()
    b = LI()
    m = max(max(a), max(b))

    # dp = [[0] * (m + 1) for _ in range(N + 1)]
    # dp[0][0] = 1
    # for i in range(N):
    #     for j in range(a[i], b[i] + 1):
    #         for k in range(0, j + 1):
    #             dp[i+1][j] += dp[i][k]
    #             dp[i+1][j] %= MOD
    # ans = sum(dp[-1]) % MOD
    # print(ans)

    dp = [[0] * (m + 2) for _ in range(N + 1)]
    for i in range(m + 1):
        dp[0][i+1] = 1

    for i in range(N):
        for j in range(a[i] + 1, m + 2):
            dp[i+1][j] = dp[i+1][j-1]
            if j <= b[i] + 1:
                dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD

    # for i in dp:
    #     print(i)

    ans = dp[-1][-1]
    print(ans)

if __name__ == '__main__':
    resolve()
