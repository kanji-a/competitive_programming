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
    a, b = LSS()
    ab = int(a + b)

    ans = 'No'
    for i in range(1, int(ab ** 0.5) + 1):
        if i ** 2 == ab:
            ans = 'Yes'
            break

    print(ans)

if __name__ == '__main__':
    resolve()
