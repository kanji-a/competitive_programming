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
    N, M = LI()
    XY = collections.defaultdict(set)
    for _ in range(M):
        X, Y = LI()
        XY[X].add(Y)

    X = [0] + list(sorted(XY.keys()))

    # Xごとの到達可能なY座標
    ans = {k:set() for k in X}
    ans[0].add(N)

    for i in range(len(X) - 1):
        # 到達可能マスのみ管理するので、配るDP
        # 到達可能なマスの、次のマスにポーンがなければ到達可能
        # 到達可能なマスの、次の両脇のマスにポーンがあれば到達可能
        for j in ans[X[i]]:
            if j not in XY[X[i+1]]:
                ans[X[i+1]].add(j)
            if 0 <= j - 1 and j - 1 in XY[X[i+1]]:
                ans[X[i+1]].add(j - 1)
            if j + 1 < 2 * N and j + 1 in XY[X[i+1]]:
                ans[X[i+1]].add(j + 1)
    # for i in X:
    #     print(i, ans[i])

    print(len(ans[X[-1]]))


if __name__ == '__main__':
    resolve()
