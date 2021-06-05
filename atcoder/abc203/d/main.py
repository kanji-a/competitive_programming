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
    A = [LI() for _ in range(N)]

    # 決め打ち二分探索

    # x以下の中央値を持つ区画はあるか
    # →xがK^2//2+1番目以下になる区画はあるか
    # →x以上の数がK^2//2+1個以下ある区画はあるか
    def is_ok(x):
        acm = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                acm[i+1][j+1] = acm[i+1][j] + (A[i][j] > x)
        for i in range(N):
            for j in range(N):
                acm[i+1][j+1] += acm[i][j+1]
        # for i in acm:
        #     print(i)
        res = False
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                num = acm[i+K][j+K] - acm[i+K][j] - acm[i][j+K] + acm[i][j]
                if num <= K ** 2 // 2:
                    res = True
        return res

    ng = -1
    ok = 10 ** 9
    while abs(ok - ng) > 1:
        m = (ng + ok) // 2
        if is_ok(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == '__main__':
    resolve()
