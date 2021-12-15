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

    # N = 16
    # for i in range(1, N + 1):
    #     print(i, N // i)

    ans = 0

    border = int(N ** 0.5)
    # N // i の値は iがN**0.5までは1個ずつ
    ans += sum(N // i for i in range(1, border + 1))

    # j = N // i の値は iがN**0.5からは1～N**0.5になる
    ans += sum(j * (N // j - N // (j + 1)) for j in range(1, border))

    print(ans)

if __name__ == '__main__':
    resolve()
