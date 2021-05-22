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
    P = [-1] * N
    P_ = LI_()
    for i in range(N - 1):
        P[i+1] = P_[i]

    print(P)
    d = [0] * N
    def f(c):
        if c != 0 and d[c] == 0:
            d[c] = f(P[c]) + 1
        return d[c]

    for i in range(N):
        f(i)

    print(d)

    Q = I()
    # 2つの条件を満たすものをカウント
    # ある頂点の子孫で深さがxのもの
    for _ in range(Q):
        U, D = LI()
        U -= 1

if __name__ == '__main__':
    resolve()
