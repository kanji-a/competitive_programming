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
    T = [SS() for _ in range(H)]

    # 有効なマスの範囲を求める
    u = 0
    d = H
    l = 0
    r = W
    for i in range(H):
        if T[i].count('#') > 0:
            u = i
            break
    for i in range(H - 1, -1, -1):
        if T[i].count('#') > 0:
            d = i + 1
            break
    for i in range(W):
        if [T[j][i] for j in range(H)].count('#') > 0:
            l = i
            break
    for i in range(W - 1, -1, -1):
        if [T[j][i] for j in range(H)].count('#') > 0:
            r = i + 1
            break
    # print(u, d, l, r)

    TT = []
    TT.append([[T[i][j] for j in range(l, r)] for i in range(u, d)])
    TT.append([[T[j][r+l-1-i] for j in range(u, d)] for i in range(l, r)])
    TT.append([[T[d+u-1-i][r+l-1-j] for j in range(l, r)] for i in range(u, d)])
    TT.append([[T[d+u-1-j][i] for j in range(u, d)] for i in range(l, r)])
    # for i in TT:
    #     for j in i:
    #         print(j)

    ans = 'No'
    for t in TT:
        h = len(t)
        w = len(t[0])
        # ハンコを押す位置
        for i in range(H + 1 - h):
            for j in range(W + 1 - w):
                is_ok = True
                # ハンコ上の位置
                for k in range(h):
                    for l in range(w):
                        if t[k][l] == '#' and S[i+k][j+l] == '#':
                            is_ok = False
                            break
                if is_ok:
                    ans = 'Yes'
                    break
    print(ans)

if __name__ == '__main__':
    resolve()

