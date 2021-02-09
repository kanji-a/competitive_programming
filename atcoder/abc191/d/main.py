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

# 入力値を10000倍して整数にする
def mul_10000(s):
    i = 0
    d = 0
    if '.' in s:
        i, d = s.split('.')
    else:
        i = s
        d = ''
    return int(i + d + '0' * (4 - len(d)))


def resolve():
    X, Y, R = [mul_10000(i) for i in LSS()]

    def binsearch(ok, ng, is_ok):
        while abs(ok - ng) > 1:
            m = (ng + ok) // 2
            if is_ok(m):
                ok = m
            else:
                ng = m
        return ok

    # 円の内部または周上の各Xに対して、Y座標の範囲を考える
    ans = 0
    scale = 10000
    for x in range(((X - R - 1) // scale + 1) * scale, ((X + R) // scale) * scale + 1, scale):
        upper = binsearch(Y - 1, Y + R + 1, lambda y: (x - X) ** 2 + (y - Y) ** 2 <= R ** 2)
        lower = binsearch(Y - R - 1, Y + 1, lambda y: (x - X) ** 2 + (y - Y) ** 2 > R ** 2)
        # print(x, upper, lower)
        ans += upper // scale - lower // scale

    print(ans)

if __name__ == '__main__':
    resolve()
