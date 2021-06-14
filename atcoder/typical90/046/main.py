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
    B = LI()
    C = LI()

    cnt_A = collections.Counter(i % 46 for i in A)
    cnt_B = collections.Counter(i % 46 for i in B)
    cnt_C = collections.Counter(i % 46 for i in C)

    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 == 0:
                    ans += cnt_A[i] * cnt_B[j] * cnt_C[k]

    print(ans)

if __name__ == '__main__':
    resolve()
