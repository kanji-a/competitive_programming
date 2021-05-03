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

    d = {0: '(', 1: ')'}
    for i in range(2 ** N):
        is_ok = True
        stk = []
        for j in range(N - 1, -1, -1):
            if i >> j & 1:
                if stk:
                    stk.pop()
                else:
                    is_ok = False
                    break
            else:
                stk.append(0)
        if not stk and is_ok:
            print(''.join(d[i >> j & 1] for j in range(N - 1, -1, -1)))

if __name__ == '__main__':
    resolve()
