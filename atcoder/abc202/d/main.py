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
    A, B, K = LI()
    K -= 1

    ans = []
    while A >= 0 and B >= 0:
        # print(A, B, K)
        if A == 0:
            for _ in range(B):
                ans.append('b')
            break
        if B == 0:
            for _ in range(A):
                ans.append('a')
            break
        x = math.comb(A + B - 1, A - 1)
        if K < x:
            ans.append('a')
            A -= 1
        else:
            ans.append('b')
            B -= 1
            K -= x

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
