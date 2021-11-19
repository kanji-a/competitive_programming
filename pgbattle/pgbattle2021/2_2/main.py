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
    T = I()
    for _ in range(T):
        N, M = LI()
        ans_min = max(N - M, 1)

        # 1つのなるべく大きな完全グラフを作る
        # M本の辺を使い切るのにいくつの頂点が必要か
        # i * (i - 1) // 2 >= Mを満たす最小のiを求める
        i = int((2 * M) ** 0.5) + 1
        if i * (i - 1) // 2 < M:
            i += 1
        ans_max = N - i + 1

        print(ans_min, ans_max)

if __name__ == '__main__':
    resolve()
