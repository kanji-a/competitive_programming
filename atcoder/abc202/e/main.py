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
    depth = [-1] * N
    ord_in = [0] * N
    ord_out = [0] * N
    depth_ord_in = [[] for _ in range(N)]
    depth_ord_out = [[] for _ in range(N)]
    def dfs(c, d):
        nonlocal cnt
        depth[c] = d
        depth_ord_in[d].append(cnt)
        ord_in[c] = cnt
        cnt += 1
        for n in G[c]:
            if depth[n] == -1:
                dfs(n, d + 1)
        depth_ord_out[d].append(cnt)
        ord_out[c] = cnt
        cnt += 1

    dfs(0, 0)
    # print(depth_ord_in)
    # print(depth_ord_out)

    Q = I()
    # inとoutがUのinとoutの間にある頂点を列挙
    for _ in range(Q):
        U, D = LI()
        U -= 1
        idx_l = bisect.bisect_left(depth_ord_in[D], ord_in[U])
        idx_r = bisect.bisect_right(depth_ord_out[D], ord_out[U])
        # print(depth_ord_in[D], ord_in[U])
        # print(depth_ord_out[D], ord_out[U])
        # print(idx_l, idx_r)
        print(max(idx_r - idx_l, 0))

if __name__ == '__main__':
    resolve()
