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
    A = LI()
    B = LI()
    C = LI_()
    A.sort()

    ans = 0
    for c in C:
        b = B[c]
        idx_l = bisect.bisect_left(A, b)
        idx_r = bisect.bisect_right(A, b)
        ans += idx_r - idx_l

    print(ans)

if __name__ == '__main__':
    resolve()
