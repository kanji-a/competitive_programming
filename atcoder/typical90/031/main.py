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
    W = LI()
    B = LI()

    max_W = max(W)
    max_B = max(B)
    dp = [[-1] * (max_W + max_B + 1) for _ in range(max_W + 1)]
    dp[0][0] = dp[0][1] = 1

    for i in range(max_W + 1):
        for j in range(max_W + max_B + 1 - i):
            if i == 0 and 0 <= j <= 1:
                continue
            # print(i, j)
            tmp = []
            for k in range(1, j // 2 + 1):
                tmp.append(dp[i][j-k])
            if 0 <= i - 1:
                tmp.append(dp[i-1][j+i])
            if tmp.count(1) >= 1:
                dp[i][j] = 0
            else:
                dp[i][j] = 1

    for i in dp:
        print(i)
    # for i, j in zip(W, B):
    #     print(dp[i][j])
    cnt = collections.Counter(dp[i][j] for i, j in zip(W, B))
    # print(cnt)

    # まず後手必勝山で勝負する。何度やっても山に対する手番は変わらない
    # 次に先手必勝山で勝負する。山が奇数個なら先手の勝ち、偶数個なら後手の勝ち。
    if cnt[0] % 2 == 1:
        print('First')
    else:
        print('Second')

if __name__ == '__main__':
    resolve()
