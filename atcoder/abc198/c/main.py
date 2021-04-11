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
    R, X, Y = LI()

    if R ** 2 > X ** 2 + Y ** 2:
        print(2)
        return 

    d_i = math.isqrt(X ** 2 + Y ** 2)
    if d_i ** 2 == X ** 2 + Y ** 2:
        ans = (d_i - 1) // R + 1
    else:
        ans = d_i // R + 1
    print(ans)

if __name__ == '__main__':
    resolve()
