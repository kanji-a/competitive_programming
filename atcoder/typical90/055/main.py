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
    N, P, Q = LI()
    A = LI()

    ans = 0
    for i in range(N - 4):
        tmp0 = A[i]
        for j in range(i + 1, N - 3):
            tmp1 = tmp0 * A[j]
            for k in range(j + 1, N - 2):
                tmp2 = tmp1 * A[k]
                for l in range(k + 1, N - 1):
                    tmp3 = tmp2 * A[l]
                    for m in range(l + 1, N):
                        tmp4 = tmp3 * A[m]
                        if tmp4 % P == Q:
                            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
