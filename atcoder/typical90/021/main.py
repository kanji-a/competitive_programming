#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
from atcoder.scc import SCCGraph
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
    scc = SCCGraph(N)
    for _ in range(M):
        A, B = LI_()
        scc.add_edge(A, B)

    ans = sum(len(i) * (len(i) - 1) // 2 for i in scc.scc())
    print(ans)

if __name__ == '__main__':
    resolve()
