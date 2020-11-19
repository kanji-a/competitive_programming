import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n
        self.diff_weight = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return r

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = w
        return True

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

def resolve():
    n, q = LI()
    wuf = WeightedUnionFind(n)
    for _ in range(q):
        query = LI()
        if query[0] == 0:
            x, y, z = query[1:]
            wuf.merge(x, y, z)
        else:
            x, y = query[1:]
            if wuf.issame(x, y):
                print(wuf.diff(x, y))
            else:
                print('?')

if __name__ == '__main__':
    resolve()
