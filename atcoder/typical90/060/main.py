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

def lis(a):
    n = len(a)
    dp = [INF] * n
    res = [0] * (n + 1)
    for i in range(n):
        idx = bisect.bisect_left(dp, a[i])
        res[i+1] = res[i] + (dp[idx] == INF)
        dp[idx] = a[i]
    return res

def resolve():
    N = I()
    A = LI()

    A_r = A[::-1]
    a = lis(A)
    a_r = lis(A_r)
    # print(a)
    # print(a_r)
    ans = 0
    for i in range(N):
        ans = max(a[i+1] + a_r[N-i] - 1, ans)
    print(ans)

if __name__ == '__main__':
    resolve()
