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
    N, L = LI()
    K = I()
    A = LI()
    AA = [A[0]]
    for i in range(N - 1):
        AA.append(A[i+1] - A[i])
    AA.append(L - A[-1])

    print(AA)
    AA.sort()
    print(AA)

if __name__ == '__main__':
    resolve()
