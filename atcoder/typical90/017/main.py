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
    N, M = LI()
    LR = [LI() for _ in range(M)]

    ans = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            aL, aR = LR[i]
            if aL > aR:
                aL, aR = aR, aL
            bL, bR = LR[j]
            if bL > bR:
                bL, bR = bR, bL
            # print(aL, aR, bL, bR)
            if aL < bL < aR < bR or bL < aL < bR < aR:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
