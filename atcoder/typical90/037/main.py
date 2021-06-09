#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
from atcoder.segtree import SegTree
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
    W, N = LI()
    LRV = [LI() for _ in range(N)]

    dp = SegTree(max, -1, W + 1)
    dp.set(0, 0)

    for i in range(N):
        L, R, V = LRV[i]
        for j in range(W, 0, -1):
            tmp = dp.prod(max(j - R, 0), max(j - L + 1, 0))
            if tmp == -1:
                dp.set(j, max(tmp, dp.get(j)))
            else:
                dp.set(j, max(tmp + V, dp.get(j)))

    print(dp.get(W))

if __name__ == '__main__':
    resolve()
