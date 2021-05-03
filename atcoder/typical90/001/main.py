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
    N, L = LI()
    K = I()
    A = LI()

    def is_ok(l):
        cnt = 0
        c = 0
        for i in range(N):
            if cnt < K and A[i] - c >= l:
                cnt += 1
                c = A[i]
        # 最後の切れ端の長さチェック
        return cnt == K and L - c >= l

    ng = L
    ok = 0
    while abs(ok - ng) > 1:
        m = (ng + ok) // 2
        if is_ok(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == '__main__':
    resolve()
