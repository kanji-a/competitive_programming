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
    A, B = LI()

    ans = []
    if A >= B:
        # 正の数は1~A、負の数は-1~-B+1と、最後に足りない分
        for i in range(1, A + 1):
            ans.append(i)
        for i in range(1, B):
            ans.append(-i)
        ans.append(-(A - B + 1) * (B + A) // 2)
    else:
        for i in range(1, B + 1):
            ans.append(-i)
        for i in range(1, A):
            ans.append(i)
        ans.append((B - A + 1) * (A + B) // 2)
    print(*ans)

if __name__ == '__main__':
    resolve()
