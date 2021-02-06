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
    N, Q = LI()
    h = LI()

    # 個別改築分の偶数番目-奇数番目
    diff = collections.Counter()
    for i in range(N - 1):
        if i % 2 == 0:
            diff[h[i] - h[i+1]] += 1
        else:
            diff[h[i+1] - h[i]] += 1

    # 一括改築分の偶数番目-奇数番目
    d = 0

    for _ in range(Q):
        Query = LI()
        if Query[0] == 1:
            v = Query[1]
            d -= v
        elif Query[0] == 2:
            v = Query[1]
            d += v
        else:
            u, v = Query[1:]
            u -= 1
            if 0 <= u - 1:
                if u % 2 == 0:
                    diff[h[u]-h[u-1]] -= 1
                    diff[h[u]-h[u-1]+v] += 1
                else:
                    diff[h[u-1]-h[u]] -= 1
                    diff[h[u-1]-h[u]-v] += 1
            if u + 1 < N:
                if u % 2 == 0:
                    diff[h[u]-h[u+1]] -= 1
                    diff[h[u]-h[u+1]+v] += 1
                else:
                    diff[h[u+1]-h[u]] -= 1
                    diff[h[u+1]-h[u]-v] += 1
            h[u] += v
        # print(h, d, diff)
        print(diff[d])

if __name__ == '__main__':
    resolve()

