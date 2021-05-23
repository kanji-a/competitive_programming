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
    P = LI_()
    G = collections.defaultdict(list)
    for i in range(N - 1):
        G[i+1].append(P[i])
        G[P[i]].append(i+1)
    # print(G)

    cnt = 0
    ord = [[0] * 2 for _ in range(N)]
    depth = [-1] * N
    def dfs(c, d):
        nonlocal cnt
        depth[c] = d
        ord[c][0] = cnt
        cnt += 1
        for n in G[c]:
            if depth[n] == -1:
                dfs(n, d + 1)
        ord[c][1] = cnt
        cnt += 1

    dfs(0, 0)
    # print(depth)
    # print(ord)
    depth_ord = [[] for _ in range(N)]
    for i in range(N):
        depth_ord[depth[i]].append(ord[i][0])
        depth_ord[depth[i]].append(ord[i][1])
    # print(depth_ord)

    Q = I()
    # inとoutがUのinとoutの間にある頂点を列挙
    for _ in range(Q):
        U, D = LI()
        U -= 1
        a = depth_ord[D]
        idx_l = bisect.bisect_left(a, ord[U][0] - 1)
        idx_r = bisect.bisect_left(a, ord[U][1] + 1)
        # print(a, ord[U], idx_l, idx_r)
        print((idx_r - idx_l) // 2)

if __name__ == '__main__':
    resolve()
