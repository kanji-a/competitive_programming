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

    # 2本でx,y(x<=y)だった場合、(y-x+1)*(x+1)
    d = [A[i+1] - A[i] for i in range(N - 1)]
    # print(d)
    ans = 1
    for i in d:
        ans *= i + 1
        ans %= MOD

    ans *= A[0] + 1
    ans %= MOD

    print(ans)

if __name__ == '__main__':
    resolve()
