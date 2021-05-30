#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
import atcoder.lazysegtree as lazysegtree
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
    
    def op(a, b):
        return max(a, b)
    e = 0
    def mapping(f, x):
        if f == -1:
            return x
        else:
            return f
    def composition(f, g):
        if f == -1:
            return g
        else:
            return f
    id_ = -1
    v = W
    lst = lazysegtree.LazySegTree(op, e, mapping, composition, id_, v)

    for _ in range(N):
        L, R = LI_()
        R += 1
        ans = lst.prod(L, R) + 1
        print(ans)
        lst.apply(L, R, ans)

if __name__ == '__main__':
    resolve()
