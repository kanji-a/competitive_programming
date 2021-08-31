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
    N, K = LI()
    XY = [LI() for _ in range(N)]

    # dp[s][i]: 点の集合sをi分割したときの答え
    dp = [[INF] * (N + 1) for _ in range(2 ** N)]
    for i in range(N + 1):
        dp[0][i] = 0

    # dd[i][j]: 点ij間の距離
    dd = [[-1] * N for _ in range(N)]
    for i in range(N):
        x0, y0 = XY[i]
        for j in range(N):
            x1, y1 = XY[j]
            dd[i][j] = (x1 - x0) ** 2 + (y1 - y0) ** 2
    print(dd)

    # d[s]: 集合s内の最大の2点間距離
    d = [-1] * (2 ** N)
    d[0] = 0
    for i in range(2 ** N):
        for j in range(N):
            if i >> j & 1:
                k = i & ~(1 << j)
                # print(bin(i), bin(k))
                tmp = 0
                for l in range(N):
                    if k >> l & 1:
                        tmp = max(dd[j][l], tmp)
                d[i] = tmp
    for i in range(2 ** N):
        print(bin(i), d[i])

    for i in range(N):
        tmp = INF
        for s in range(1, 2 ** N):
            ss = s
            # sの部分集合全てを走査
            while ss > 0:
                ss = (ss - 1) & s
                tmp = min(max(dp[s^ss][i-1], d[ss]), tmp)
            dp[s][i] = tmp

    for i in range(2 ** N):
        print(bin(i), dp[i])
    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
