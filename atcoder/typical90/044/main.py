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
    N, Q = LI()
    A = LI()

    shift = 0
    for _ in range(Q):
        T, x, y = LI_()
        if T == 0:
            x_ = (x - shift) % N
            y_ = (y - shift) % N
            A[x_], A[y_] = A[y_], A[x_]
        elif T == 1:
            shift += 1
        else:
            print(A[(x - shift) % N])

if __name__ == '__main__':
    resolve()
