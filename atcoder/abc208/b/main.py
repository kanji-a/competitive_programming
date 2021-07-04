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
    P = I()

    c = [1]
    for i in range(2, 11):
        c.append(c[-1] * i)
    # print(c)

    ans = 0
    for i in range(9, -1, -1):
        ans += P // c[i]
        P %= c[i]
    print(ans)

if __name__ == '__main__':
    resolve()
