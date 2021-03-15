#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
from atcoder.dsu import DSU
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    f = LI_()

    # 2 ** 連結成分数 - 1
    dsu = DSU(N)
    for i, e in enumerate(f):
        dsu.merge(i, e)
    lc_num = len(set(dsu.leader(i) for i in range(N)))

    ans = pow(2, lc_num, MOD) - 1
    print(ans)

if __name__ == '__main__':
    resolve()
