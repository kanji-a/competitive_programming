#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
from atcoder.mincostflow import MCFGraph
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
    ac = [LSS() for _ in range(2 * N)]

    # 2分マッチング
    mcfg = MCFGraph(4 * N + 2)
    for i in range(2 * N):
        mcfg.add_edge(4 * N, i, 1, 0)
        mcfg.add_edge(2 * N + i, 4 * N + 1, 1, 0)
    for i in range(2 * N):
        for j in range(2 * N):
            if i == j:
                continue
            k = 2 * N + j
            if ac[i][1] == ac[j][1]:
                mcfg.add_edge(i, k, 1, 0)
            else:
                mcfg.add_edge(i, k, 1, abs(int(ac[i][0]) - int(ac[j][0])))

    # print(mcfg.edges())
    f = mcfg.flow(4 * N, 4 * N + 1, 2 * N)
    # print(mcfg.edges())
    print(f[1] // 2)

if __name__ == '__main__':
    resolve()
