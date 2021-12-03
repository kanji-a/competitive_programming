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
    a = LI()

    c = collections.Counter(a)

    # OKな必要十分条件: ベスト1が1人、ベスト2^xが2^(x-1)人であること。
    # aは2の累乗という条件があるので、ベスト1が1人、ベストxがx//2人であること、でよい。

if __name__ == '__main__':
    resolve()
