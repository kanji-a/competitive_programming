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

def resolve():
    H, W = LI()
    S = [SS() for _ in range(H)]

    # 方向
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # 辺を始点: 方向 の形式で保持
    edge = {}
    for i in range(H - 1):
        for j in range(W):
            if S[i][j] == '.' and S[i+1][j] == '#':
                edge[(i + 1, j)] = 0
            if S[i][j] == '#' and S[i+1][j] == '.':
                edge[(i + 1, j + 1)] = 2
    for i in range(H):
        for j in range(W - 1):
            if S[i][j] == '#' and S[i][j+1] == '.':
                edge[(i, j + 1)] = 1
            if S[i][j] == '.' and S[i][j+1] == '#':
                edge[(i + 1, j + 1)] = 3
    # print(edge)

    # 辺を一周して方向転換があるかチェック
    ans = 0
    dir_p = -1
    sy, sx = min((edge.keys()))
    cy, cx = sy, sx
    is_started = False
    while not is_started or (cy, cx) != (sy, sx):
        is_started = True
        dir = edge[(cy, cx)]
        if dir != dir_p:
            ans += 1
            dir_p = dir
        dy, dx = d[dir]
        cy += dy
        cx += dx

    print(ans)

if __name__ == '__main__':
    resolve()
