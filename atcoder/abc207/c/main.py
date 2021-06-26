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
    tlr = [LI() for _ in range(N)]

    ans = 0
    for i in range(N - 1):
        t1, l1, r1 = tlr[i]
        if t1  in (3, 4):
            l1 += 0.5
        if t1  in (2, 4):
            r1 -= 0.5
        for j in range(i + 1, N):
            t2, l2, r2 = tlr[j]
            if t2  in (3, 4):
                l2 += 0.5
            if t2  in (2, 4):
                r2 -= 0.5
            # print(l1, r1, l2, r2)
            if l2 <= r1 and l1 <= r2:
                ans += 1
    print(ans)

if __name__ == '__main__':
    resolve()
