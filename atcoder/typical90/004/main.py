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
    H, W = LI()
    A = [LI() for _ in range(H)]

    sum_r = [sum(i) for i in A]
    sum_c = [sum(A[j][i] for j in range(H)) for i in range(W)]
    # print(sum_r)
    # print(sum_c)

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = sum_r[i] + sum_c[j] - A[i][j]

    for i in ans:
        print(*i)

if __name__ == '__main__':
    resolve()
