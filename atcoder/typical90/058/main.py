#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 5
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()

    def f(x):
        x_tmp = x
        y = 0
        while x_tmp > 0:
            y += x_tmp % 10
            x_tmp //= 10
        z = (x + y) % MOD
        return z

    # xはρ型に変化する
    x = N
    order = []
    visited = set()
    head = -1
    for _ in range(K):
        x = f(x)
        if x in visited:
            head = x
            break
        order.append(x)
        visited.add(x)
        # print(x)
    # print(head)
    # print(order)

    if head == -1:
        print(order[K-1])
    else:
        len_bar = order.index(head)
        len_cycle = len(order) - len_bar
        idx = len_bar + (K - len_bar - 1) % len_cycle
        ans = order[idx]
        # print(len_bar, len_cycle, len(order))
        print(ans)

if __name__ == '__main__':
    resolve()
