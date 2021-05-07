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
    CP = [LI() for _ in range(N)]
    acm = [[0] * (N + 1) for _ in range(2)]

    for i in range(N):
        C, P = CP[i]
        C -= 1
        acm[C][i+1] = acm[C][i] + P
        acm[1-C][i+1] = acm[1-C][i]

    Q = I()
    for _ in range(Q):
        L, R = LI_()
        print(acm[0][R+1] - acm[0][L], acm[1][R+1] - acm[1][L])

if __name__ == '__main__':
    resolve()
