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
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    # order[i][j] = k
    # i:連結成分番号, j:順番, k:頂点番号
    order = []
    visited = [False] * N

    # 探索順を決める
    def dfs1(c, con):
        visited[c] = True
        con.append(c)
        for n in G[c]:
            if not visited[n]:
                dfs1(n, con)

    for i in range(N):
        con = []
        if not visited[i]:
            dfs1(i, con)
            order.append(con)
    # print(order)

    # 塗りパターンを数える
    color = [-1] * N
    def dfs2(o, d, tmp):
        c = o[d]
        # 今見ている頂点に塗れる色
        s = set([0, 1, 2]) - set(color[i] for i in G[c])
        # print(o, d, tmp, color, s)
        if d == len(o) - 1:
            tmp[0] += len(s)
            return
        for i in s:
            color[c] = i
            if d + 1 < len(o):
                dfs2(o, d + 1, tmp)       
            color[c] = -1

    ans = 1
    for i in order:
        # TODO: 参照を使いたいためだけに単一の値を配列で持つのをやめる
        tmp = [0]
        dfs2(i, 0, tmp)
        ans *= tmp[0]

    print(ans)

if __name__ == '__main__':
    resolve()
