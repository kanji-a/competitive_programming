#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.par[x] = r
            return r

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        return True

def resolve():
    N = I()
    f = LI_()

    # 2 ** 連結成分数 - 1
    uf = UnionFind(N)
    for i, e in enumerate(f):
        uf.merge(i, e)
    lc_num = len(set(uf.root(i) for i in range(N)))

    ans = pow(2, lc_num, MOD) - 1
    print(ans)

if __name__ == '__main__':
    resolve()
