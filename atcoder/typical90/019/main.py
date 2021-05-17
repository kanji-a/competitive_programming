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
    A = LI()

    dp = [[INF] * (2 * N + 1) for _ in range(2 * N + 1)]
    for i in range(2 * N + 1):
        dp[i][i] = 0

    # 区間の長さ
    for l in range(2, 2 * N + 1, 2):
        # 区間の左端
        for i in range(0, 2 * N - l + 1):
            tmp = INF
            # 取り除く数の左側
            for j in range(i, i + l - 1):
                # print(l, i, i+l, j)
                tmp = min(dp[i][j+1] + dp[j+1][i+l], tmp)
            dp[i][i+l] = min(dp[i+1][i+l-1] + abs(A[i] - A[i+l-1]), tmp)
    # for i in dp:
    #     print(i)

    print(dp[0][-1])

if __name__ == '__main__':
    resolve()
