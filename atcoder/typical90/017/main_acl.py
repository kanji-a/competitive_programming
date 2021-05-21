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
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
# from atcoder.fenwicktree import FenwickTree
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
    N, M = LI()
    LR = [LI_() for _ in range(M)]

    # 余事象を考える
    ans = M * (M - 1) // 2

    # 1. 端点が一致する場合
    cnt = collections.Counter()
    for i, j in LR:
        cnt[i] += 1
        cnt[j] += 1
    num1 = sum(i * (i - 1) // 2 for i in cnt.values())

    # 2. 重複が無い場合
    # 各Lに対して、R<LとなるRをカウントする
    cnt = [0] * N
    for _, i in LR:
        cnt[i] += 1
    acm = list(itertools.accumulate(cnt, initial=0))
    # print(acm)
    num2 = 0
    for i, _ in LR:
        num2 += acm[i]
    # num2_ = 0
    # for i in range(M - 1):
    #     for j in range(i + 1, M):
    #         aL, aR = LR[i]
    #         bL, bR = LR[j]
    #         if aR < bL or bR < aL:
    #             num2_ += 1

    # 3. 包含関係にある場合
    LR.sort(key=lambda x: x[1])
    # Rの小さい順に線分を追加していって、追加した線分よりLが大きい線分を数える
    # Rを小さい順に追加することで、Lだけを見ればよくなる
    fwt = FenwickTree(N)
    num3 = 0
    for L, R in LR:
        if L + 1 <= R - 1:
            num3 += fwt.sum(L + 1, R - 1)
        fwt.add(L, 1)

    # print(num1, num2, num2_, num3)
    ans = ans - num1 - num2 - num3
    print(ans)

if __name__ == '__main__':
    resolve()
