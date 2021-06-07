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

    X = list(sorted(XY.keys()))

    # 到達可能なY座標
    ans = set()
    ans.add(N)

    for i in range(len(X)):
        # ポーンがないマスの到達は手前そのまま
        # ポーンがあるマスの斜め前に到達可能なら到達可能
        ok = set()
        ng = set()
        for j in XY[X[i]]:
            # print(i, j, ans)
            if 0 <= j - 1 and j - 1 in ans or j + 1 <= 2 * N and j + 1 in ans:
                ok.add(j)
            else:
                ng.add(j)
        ans -= ng
        ans |= ok
        # print(ans)

    print(len(ans))

if __name__ == '__main__':
    resolve()
