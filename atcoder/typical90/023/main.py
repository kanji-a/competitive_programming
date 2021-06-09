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
    C = [SS() for _ in range(W)]

    # bitDP 今の行の置き方に影響を与えるのは1行前の状態のみ
    dp = [[0] * 2 ** W for _ in range(H)]
    for i in range(2 ** W):
        # #に置くパターンは弾く
        is_ok = True
        for j in range(W):
            if i >> j and C[0][j] == '#':
                is_ok = False
                break
        # そのマスに置けるか
        tmp = [True] * W
        for j in range(W):
            if i >> j:
                if 0 <= j - 1:
                    tmp[j-1] = False
                if j + 1 < W:
                    tmp[j+1] = False
        is_ok = True
        for j in range(W):
            if i >> j and not tmp[j]:
                is_ok = False
                break
        if is_ok:
            dp[0][i] = 1
    print(dp[0])


    # for i in range(H - 1):
    #     for j in range(2 ** W):
    #         for k in range(2 ** W):

if __name__ == '__main__':
    resolve()
