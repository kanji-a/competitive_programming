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
    N, K = LI()
    A = [LI() for _ in range(N)]

    # 決め打ち二分探索 → 中央値作れるか2分できなさそう
    # K*Kの区画を全探索 → 間に合わない
    # 中央値が低いを言い換える
    ans = INF
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            tmp = []
            for k in range(K):
                for l in range(K):
                    tmp.append(A[i+k][j+l])
            tmp.sort(reverse=True)
            # print(tmp)
            ans = min(tmp[K**2//2], ans)
    print(ans)

if __name__ == '__main__':
    resolve()
