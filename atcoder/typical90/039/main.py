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
    G = collections.defaultdict(list)
    for _ in range(N - 1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    # 辺ごとの登場回数を集計する
    desc = [0] * N

    def dfs(c, p):
        sum_desc = 1
        child_count = 0
        for n in G[c]:
            if n != p:
                child_count += 1
                dfs(n, c)
                sum_desc += desc[n]
        desc[c] = sum_desc

    dfs(0, -1)
    # print(desc)

    # 各辺の登場回数は、深い方の頂点とその子孫と、それ以外の頂点の積
    # 木なので各辺を頂点に対応付けられる
    ans = sum(desc[i] * (N - desc[i]) for i in range(N))
    print(ans)

if __name__ == '__main__':
    resolve()
