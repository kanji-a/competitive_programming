#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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

    ans = 'Yes'
    t_pre = 0
    x_pre = 0
    y_pre = 0
    for _ in range(N):
        t, x, y = LI()
        t_d = t - t_pre
        x_d = abs(x - x_pre)
        y_d = abs(y - y_pre)
        t_pre = t
        x_pre = x
        y_pre = y
        if x_d + y_d > t_d or (t_d - x_d - y_d) % 2 == 1:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    resolve()
