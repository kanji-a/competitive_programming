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
    AB = [LI() for _ in range(N)]

    ans = INF
    for i in range(N - 1):
        for j in range(i, N):
            # print(AB[i], AB[j])
            if i == j:
                ans = min(AB[i][0] + AB[j][1], ans)
            else:
                ans = min(max(AB[i][0], AB[j][1]), max(AB[j][0], AB[i][1]), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
