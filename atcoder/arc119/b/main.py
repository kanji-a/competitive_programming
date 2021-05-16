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
    S = SS()
    T = SS()

    idx_0_S = []
    idx_0_T = []
    for i in range(N):
        if S[i] == '0':
            idx_0_S.append(i)
        if T[i] == '0':
            idx_0_T.append(i)
    # print(idx_0_S)
    # print(idx_0_T)

    if len(idx_0_S) != len(idx_0_T):
        print(-1)
        return

    ans = len([(i, j) for i, j in zip(idx_0_S, idx_0_T) if i != j])
    print(ans)

if __name__ == '__main__':
    resolve()
