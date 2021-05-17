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

    # lから奇数番目の和と偶数番目の和が等しいことが0にできる必要十分条件
    acm = [0] * (N + 1)
    for i in range(N):
        if i % 2 == 0:
            acm[i+1] = acm[i] + A[i]
        else:
            acm[i+1] = acm[i] - A[i]
    # print(acm)

    d = collections.Counter(acm)
    ans = sum(i * (i - 1) // 2 for i in d.values())

    print(ans)

if __name__ == '__main__':
    resolve()
