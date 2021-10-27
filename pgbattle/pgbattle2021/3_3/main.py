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
    R = LI()

    # p[i]: x==iになる確率
    l = N + max(R) + 1
    p = [0] * l
    p[1] = 1

    for i in range(1, N + 1):
        # print(p)
        for j in range(1, R[i-1] + 1):
            p[i+j] += p[i] * (R[i-1] - j + 1) * pow(R[i-1] * (R[i-1] + 1) // 2, MOD - 2, MOD)
            # p[i+j] += p[i] * (R[i-1] - j + 1) / (R[i-1] * (R[i-1] + 1) // 2)
            p[i+j] %= MOD

    # print(p)

    ans = sum(i * p[i] % MOD for i in range(N + 1, l))
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    resolve()
