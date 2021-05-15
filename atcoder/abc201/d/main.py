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
    H, W = LI()
    A = [SS() for _ in range(H)]

    # この先の先手得点-後手得点
    dp = [[0] * W for _ in range(H)]
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if i == H - 1 and j == W - 1:
                continue
            # 先手
            if (i + j) % 2 == 0:
                # 下
                tmp_d = -INF
                if i + 1 < H:
                    if A[i+1][j] == '+':
                        tmp_d = dp[i+1][j] + 1
                    else:
                        tmp_d = dp[i+1][j] - 1
                # 右
                tmp_r = -INF
                if j + 1 < W:
                    if A[i][j+1] == '+':
                        tmp_r = dp[i][j+1] + 1
                    else:
                        tmp_r = dp[i][j+1] - 1
                dp[i][j] = max(tmp_d, tmp_r)
            # 後手
            else:
                tmp_d = INF
                # 下
                if i + 1 < H:
                    if A[i+1][j] == '+':
                        tmp_d = dp[i+1][j] - 1
                    else:
                        tmp_d = dp[i+1][j] + 1
                # 右
                tmp_r = INF
                if j + 1 < W:
                    if A[i][j+1] == '+':
                        tmp_r = dp[i][j+1] - 1
                    else:
                        tmp_r = dp[i][j+1] + 1
                dp[i][j] = min(tmp_d, tmp_r)
    # for i in dp:
    #     print(i)

    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    resolve()
