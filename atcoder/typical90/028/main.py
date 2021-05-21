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
    N = I()
    lxlyrxry = [LI() for _ in range(N)]

    x_max = max(i[2] for i in lxlyrxry)
    y_max = max(i[3] for i in lxlyrxry)

    imos = [[0] * (y_max + 1) for _ in range(x_max + 1)]
    for i, j, k, l in lxlyrxry:
        imos[i][j] += 1
        imos[k][j] -= 1
        imos[i][l] -= 1
        imos[k][l] += 1
    # for i in imos:
    #     print(i)

    for i in range(x_max):
        for j in range(y_max + 1):
            imos[i+1][j] += imos[i][j]
    # for i in imos:
        # print(i)
    for i in range(x_max):
        for j in range(y_max):
            imos[i][j+1] += imos[i][j]
    # for i in imos:
    #     print(i)

    cnt = collections.Counter()
    for i in range(x_max + 1):
        for j in range(y_max + 1):
            cnt[imos[i][j]] += 1
    for i in range(1, N + 1):
        print(cnt[i])

if __name__ == '__main__':
    resolve()
