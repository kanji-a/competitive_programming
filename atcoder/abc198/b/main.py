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
    N = SS()
    len_N = len(N)

    idx = len_N
    for i in range(len_N - 1, -1, -1):
        if N[i] != '0':
            idx = i
            break
    NN = N[:idx+1]

    if NN == NN[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
