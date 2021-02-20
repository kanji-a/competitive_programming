#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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

def base_n(X, n):
    res = 0
    tmp = 1
    for i in reversed(X):
        res += tmp * int(i)
        tmp *= n
    return res

def resolve():
    X = SS()
    M = I()

    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    d = max([int(i) for i in X])
    # どこでMを超えるかを二分探索
    ng = M + 1
    ok = d
    while abs(ng - ok) > 1:
        m = (ng + ok) // 2
        if base_n(X, m) <= M:
            ok = m
        else:
            ng = m
    
    ans = ok - d
    print(ans)

if __name__ == '__main__':
    resolve()
