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
    DCS = [LI() for _ in range(N)]
    DCS.sort(key=lambda x: x[0])
    # print(DCS)

    max_D = DCS[-1][0]

    # dp[i][j]: [:i]番目を選んだときの[:j]日目までの最大報酬
    dp = [[0] * (max_D + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(max_D + 1):
            d, c, s = DCS[i]
            if c <= j <= d:
                # 仕事iができる場合
                dp[i+1][j] = max(dp[i][j-c] + s, dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    # for i in dp:
    #     print(i)

    print(max(dp[-1]))

if __name__ == '__main__':
    resolve()
