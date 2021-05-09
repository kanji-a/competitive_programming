#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
from atcoder.dsu import DSU
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
    H, W = LI()
    Q = I()

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    red = [[False] * W for _ in range(H)]
    dsu = DSU(H * W)

    for _ in range(Q):
        q = LI()
        if q[0] == 1:
            r, c = q[1:]
            r -= 1
            c -= 1
            red[r][c] = True
            for dy, dx in d:
                ny = r + dy
                nx = c + dx
                if 0 <= ny < H and 0 <= nx < W and red[ny][nx]:
                    cur = r * W + c
                    nxt = ny * W + nx
                    dsu.merge(cur, nxt)
        else:
            ra, ca, rb, cb = q[1:]
            ra -= 1
            ca -= 1
            rb -= 1
            cb -= 1
            a = ra * W + ca
            b = rb * W + cb
            if red[ra][ca] and red[rb][cb] and dsu.same(a, b):
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    resolve()
