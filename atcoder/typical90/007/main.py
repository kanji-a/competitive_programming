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
    A.sort()
    Q = I()
    for _ in range(Q):
        B = I()
        idx = bisect.bisect_left(A, B)
        ans = min(abs(A[max(idx-1, 0)] - B), abs(A[min(idx, N-1)] - B))
        print(ans)

if __name__ == '__main__':
    resolve()
