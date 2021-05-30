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
    N, K = LI()
    AB = [LI() for _ in range(N)]
    AB.sort()

    c = 0
    for i in range(N):
        # print(c, K)
        a, b = AB[i]
        if a - c <= K:
            K -= a - c
            K += b
            c = a
        else:
            break
    print(c + K)

if __name__ == '__main__':
    resolve()
