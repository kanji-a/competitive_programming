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
    A = LI()
    A.sort()

    med_A = 0
    if N % 2 == 1:
        med_A = A[N//2]
    else:
        med_A = (A[N//2] + A[N//2-1]) / 2
    # print(med_A)
    ans = sum(med_A / 2 + i - min(i, med_A) for i in A) / N
    print(ans)

if __name__ == '__main__':
    resolve()
