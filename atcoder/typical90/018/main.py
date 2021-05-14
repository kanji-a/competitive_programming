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
    T = I()
    L, X, Y = LI()
    Q = I()
    for _ in range(Q):
        E = I()
        theta = 2 * math.pi * E / T
        y = -L / 2 * math.sin(theta)
        z = L / 2 * (1 - math.cos(theta))
        ans = math.atan2(z, (X ** 2 + (Y - y) ** 2) ** 0.5) * 180 / math.pi
        print(ans)

if __name__ == '__main__':
    resolve()
