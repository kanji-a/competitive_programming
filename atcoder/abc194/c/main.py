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

    cnt = collections.Counter(A)
    ans = 0
    for k1, v1 in cnt.items():
        for k2, v2 in cnt.items():
            ans += (k1 - k2) ** 2 * v1 * v2
    ans //= 2

    print(ans)

if __name__ == '__main__':
    resolve()
