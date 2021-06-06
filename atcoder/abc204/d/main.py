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
    N = I()
    T = LI()
    sum_T = sum(T)

    dp = [False] * (sum_T + 1)
    dp[0] = True
    for i in range(N):
        for j in range(sum_T, -1, -1):
            if j - T[i] >= 0:
                dp[j] = max(dp[j - T[i]], dp[j])
    # print(dp)

    ans = sum_T
    for i in range(sum_T + 1):
        if dp[i]:
            ans = min(max(i, sum_T - i), ans)
    
    print(ans)

if __name__ == '__main__':
    resolve()
