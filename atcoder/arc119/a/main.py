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

    b_max = 0
    while 2 ** (b_max + 1) < N:
        b_max += 1
    # print(b_max)

    ans = INF
    for b in range(b_max + 1):
        a = N // 2 ** b
        c = N - a * 2 ** b
        ans = min(a + b + c, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
