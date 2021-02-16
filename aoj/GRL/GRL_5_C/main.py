#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    n = I()
    G = collections.defaultdict(list)
    for i in range(n):
        G[i] = LI()[1:]

    depth = [0] * n
    par = [-1] * n

    que = collections.deque()
    que.append(0)
    while que:
        cur = que.popleft()
        for nxt in G[cur]:
            depth[nxt] = depth[cur] + 1
            par[nxt] = cur
            que.append(nxt)
    # print(depth)
    # print(par)

    # ダブリング配列準備
    par[0] = 0
    log_h = max(max(depth).bit_length(), 1)
    doubling = [[-1] * n for _ in range(log_h)]
    for i in range(n):
        doubling[0][i] = par[i]
    for i in range(log_h - 1):
        for j in range(n):
            doubling[i+1][j] = doubling[i][doubling[i][j]]
    # print(doubling)

    q = I()
    for _ in range(q):
        u, v = LI()
        # 高さを揃える
        # uの方が深いとする
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for i in range(d.bit_length()):
            if d >> i & 1:
                u = doubling[i][u]
        # 二分探索でLCAを求める
        if u == v:
            print(u)
            continue
        for i in range(log_h - 1, -1, -1):
            if doubling[i][u] != doubling[i][v]:
                u = doubling[i][u]
                v = doubling[i][v]
        print(par[u])

if __name__ == '__main__':
    resolve()
