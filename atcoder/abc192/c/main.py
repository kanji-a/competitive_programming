#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    N, K = LI()

    def f(x):
        x_s = list(str(x))
        g1 = int(''.join(sorted(x_s, reverse=True)))
        g2 = int(''.join(sorted(x_s)))
        res = g1 - g2
        return res

    a = N
    for _ in range(K):
        a = f(a)

    print(a)

if __name__ == '__main__':
    resolve()
