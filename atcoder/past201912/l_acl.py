import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder_dsu_code = """
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
"""

atcoder.dsu = types.ModuleType('atcoder.dsu')
exec(_atcoder_dsu_code, atcoder.dsu.__dict__)
DSU = atcoder.dsu.DSU

import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
# from atcoder.dsu import DSU
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

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    dsu = DSU(V)
    res = 0
    for e in es:
        if not dsu.same(e[0], e[1]):
            dsu.merge(e[0], e[1])
            res += e[2]
    return res

def resolve():
    N, M = LI()
    E = []
    xyc = [LI() for _ in range(N)]
    for i, j in itertools.combinations(range(N), 2):
        x0, y0, c0 = xyc[i]
        x1, y1, c1 = xyc[j]
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        if c0 != c1:
            d *= 10
        E.append((i, j, d))
    XYC = [LI() for _ in range(M)]

    # 全ての小さい塔の組み合わせに対してBIT全探索してMST
    ans = INF
    for i in range(2 ** M):
        EE = copy.deepcopy(E)
        # 小さい塔同士の辺
        for j, k in itertools.combinations(range(M), 2):
            if i >> j & 1 and i >> k & 1:
                X0, Y0, C0 = XYC[j]
                X1, Y1, C1 = XYC[k]
                d = ((X1 - X0) ** 2 + (Y1 - Y0) ** 2) ** 0.5
                if C0 != C1:
                    d *= 10
                EE.append((N + j, N + k, d))
        # 小さい塔から大きい塔への辺
        for j in range(M):
            if i >> j & 1:
                X, Y, C = XYC[j]
                for k in range(N):
                    x, y, c = xyc[k]
                    d = ((X - x) ** 2 + (Y - y) ** 2) ** 0.5
                    if C != c:
                        d *= 10
                    EE.append((N + j, k, d))
        ans = min(kruskal(EE, N + M), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
