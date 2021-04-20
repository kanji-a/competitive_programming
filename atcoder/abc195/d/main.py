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
    N, M, Q = LI()
    WV = [LI() for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X = LI()
    for _ in range(Q):
        L, R = LI()
        XX = []
        for i in range(0, M):
            if i < L - 1 or R <= i:
                XX.append(X[i])
        cnt = collections.Counter(XX)
        # print(XX)
        ans = 0
        for i, j in WV:
            # Vが高い順にギリギリ入る箱に入れていく
            tmp = INF
            for k in cnt.keys():
                if k >= i and cnt[k] > 0:
                    tmp = min(k, tmp)
            if tmp != INF:
                cnt[tmp] -= 1
                ans += j
        # print(cnt)
        print(ans)

if __name__ == '__main__':
    resolve()
