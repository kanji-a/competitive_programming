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
    A = [SS() for _ in range(2 * N)]
    d = {'G': 0, 'C': 1, 'P': 2}

    points = [0] * (2 * N)
    # rank[順位]: 選手番号
    rank = list(range(2 * N))

    for i in range(M):

        # 試合
        for j in range(N):
            num0, num1 = rank[2*j], rank[2*j+1]
            te0, te1 = d[A[num0][i]], d[A[num1][i]]
            if (te1 - te0) % 3 == 1:
                points[num0] += 1
            if (te0 - te1) % 3 == 1:
                points[num1] += 1

        # ランキング更新
        tmp = sorted(enumerate(points), key=lambda x: (-x[1], x[0]))
        # print(tmp)
        rank = [i[0] for i in tmp]

        # print(points, rank)

    for i in range(2 * N):
        print(rank[i] + 1)

if __name__ == '__main__':
    resolve()
