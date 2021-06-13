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

    num_p = 1
    num_m = 1
    ans_p = A[-1]
    ans_m = -A[-1]
    for i in range(N - 2, -1, -1):
        num_p, num_m = (num_p + num_m) % MOD, num_p % MOD
        # print(num_p, num_m)
        ans_p, ans_m = (num_p * A[i] + ans_p + ans_m) % MOD, (-num_m * A[i] + ans_p) % MOD
        # print(ans_p, ans_m)
    print(ans_p)

if __name__ == '__main__':
    resolve()
