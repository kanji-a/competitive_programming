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
    N = I()
    S = [SS() for _ in range(N)]

    # dp[i][j]: y_iがjになるものの個数
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(N):
        if S[i] == 'AND':
            dp[i+1][1] = dp[i][1]
            dp[i+1][0] = dp[i][0] * 2 + dp[i][1]
        else:
            dp[i+1][1] = dp[i][0] + dp[i][1] * 2
            dp[i+1][0] = dp[i][0]
    # print(dp)

    print(dp[-1][1])

if __name__ == '__main__':
    resolve()

