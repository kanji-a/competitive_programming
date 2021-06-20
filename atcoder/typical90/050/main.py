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
    N, L = LI()

    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(N):
        if i + 1 - L >= 0:
            dp[i+1] = dp[i+1-L] + dp[i]
        else:
            dp[i+1] = dp[i]
        dp[i+1] %= MOD
    # print(dp)

    print(dp[-1])

if __name__ == '__main__':
    resolve()
