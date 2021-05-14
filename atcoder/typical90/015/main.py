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

def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i) % p
        denom = denom * i % p
    return numer * pow(denom, p-2, p) % p

def resolve():
    N = I()

    # 差の最小値
    for k in range(1, N + 1):
        ans = 0
        # 取るボールの数
        for r in range(1, (N - 1) // k + 2):
            ans += combMod(N - (k - 1) * (r - 1), r, MOD)
            ans %= MOD
        print(ans)

if __name__ == '__main__':
    resolve()
