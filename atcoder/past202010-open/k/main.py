import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder_fenwicktree_code = """
import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s
"""

atcoder.fenwicktree = types.ModuleType('atcoder.fenwicktree')
exec(_atcoder_fenwicktree_code, atcoder.fenwicktree.__dict__)
FenwickTree = atcoder.fenwicktree.FenwickTree

#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
# from atcoder.fenwicktree import FenwickTree
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    K = I()
    n = []
    a = []
    for _ in range(K):
        n.append(I())
        a.append(LI())
    Q = I()
    b = LI_()

    # 事前にそれぞれのaの転倒数を計算する
    a_inv_num = [0] * K
    for i in range(K):
        fwt = FenwickTree(21)
        tmp = 0
        for j in range(n[i]):
            fwt.add(a[i][j], 1)
            tmp += fwt.sum(a[i][j] + 1, 21)
            tmp %= MOD
        a_inv_num[i] = tmp
    # print(a_inv_num)

    ans = 0
    # 操作ごとに増える転倒数を足していく
    # 増加分は、a[b[i]]の転倒数と、x内のa[b[i]]の要素ごとの転倒している数字の個数
    fwt = FenwickTree(21)
    for i in b:
        ans += a_inv_num[i]
        for j in range(n[i]):
            ans += fwt.sum(a[i][j] + 1, 21)
            ans %= MOD
        cnt = [0] * 21
        for j in range(n[i]):
            cnt[a[i][j]] += 1
        for j in range(21):
            fwt.add(j, cnt[j])
    print(ans)

if __name__ == '__main__':
    resolve()

