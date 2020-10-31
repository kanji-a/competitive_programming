import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
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
        self.parents = [-1] * n

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

def factorialMod(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= MOD
    return res

def resolve():
    N, K = LI()
    a = [LI() for _ in range(N)]

    # 行スワップと列スワップは独立

    # どの行(列)とどの行(列)がスワップできるか探索
    # グラフを作って連結成分の大きさを探索し、その階乗を掛け合わせる
    uf_r = UnionFind(N)
    for i, j in itertools.combinations(range(N), 2):
        if [a[i][k] + a[j][k] <= K for k in range(N)].count(False) == 0:
            uf_r.unite(i, j)
    sizes_r = [-i for i in uf_r.parents if i < 0]
    # print(sizes_r)

    uf_c = UnionFind(N)
    for i, j in itertools.combinations(range(N), 2):
        if [a[k][i] + a[k][j] <= K for k in range(N)].count(False) == 0:
            uf_c.unite(i, j)
    sizes_c = [-i for i in uf_c.parents if i < 0]
    # print(sizes_c)
    
    ans = 1
    for i in sizes_r:
        ans *= factorialMod(i)
        ans %= MOD
    for i in sizes_c:
        ans *= factorialMod(i)
        ans %= MOD

    print(ans)

if __name__ == '__main__':
    resolve()
