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
    N = I()
    A = [LI() for _ in range(N)]
    M = I()
    XY_ = [LI_() for _ in range(M)]
    XY = set()
    for i, j in XY_:
        XY.add((i, j))
        XY.add((j, i))

    ans = INF
    for i in itertools.permutations(range(N)):
        is_ok = True
        for j in range(N - 1):
            if (i[j], i[j+1]) in XY:
                is_ok = False
                break
        if is_ok:
            t = 0
            for j, e in enumerate(i):
                t += A[e][j]
            ans = min(t, ans)

    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    resolve()
