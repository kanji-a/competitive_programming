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

class UnionFind():
    def __init__(self, n, C):
        self.n = n
        self.parents = [-1] * n
        self.sizes_class = [collections.Counter() for _ in range(n)]
        for i in range(n):
            self.sizes_class[i][C[i]] = 1

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        # for k, v in self.sizes_class[y]:
        #     self.sizes_class[x][k] += v
        self.sizes_class[x] += self.sizes_class[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
    N, Q = LI()
    C = LI()
    uf = UnionFind(N, C)
    for _ in range(Q):
        Query = LI()
        if Query[0] == 1:
            a = Query[1] - 1
            b = Query[2] - 1
            if not uf.same(a, b):
                uf.unite(a, b)
            # print(uf.sizes_class)
        else:
            x = Query[1] - 1
            y = Query[2]
            print(uf.sizes_class[uf.find(x)][y])

if __name__ == '__main__':
    resolve()
