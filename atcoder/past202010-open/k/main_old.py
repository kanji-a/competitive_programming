#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
from atcoder.fenwicktree import FenwickTree
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
        for j in range(n[i]):
            fwt.add(a[i][j], 1)
    print(ans)

if __name__ == '__main__':
    resolve()

