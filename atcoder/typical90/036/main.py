#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
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
    N, Q = LI()
    xy = [LI() for _ in range(N)]

    # 45度回転(と拡大)することで、(x, y)は(x+y, x-y)に移動
    # 元のマンハッタン距離は回転後にmax(x座標の差, y座標の差)になった
    xxyy = [(x - y, x + y) for x, y in xy]

    # 一番離れているのは端っこにいるどれか
    min_xx = min(xx for xx, __ in xxyy)
    max_xx = max(xx for xx, __ in xxyy)
    min_yy = min(yy for __, yy in xxyy)
    max_yy = max(yy for __, yy in xxyy)

    for _ in range(Q):
        q = I() - 1
        x, y = xy[q]
        xx = x - y
        yy = x + y
        ans = max(xx - min_xx, max_xx - xx, yy - min_yy, max_yy - yy)
        print(ans)

if __name__ == '__main__':
    resolve()
