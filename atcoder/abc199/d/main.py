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

    ans = 0
    color = [-1] * N

    def dfs(c):
        # if len(available_colors) == 0:
        #     return
        # for i in available_colors:
        #     color[c] = i
        available_colors = set([0, 1, 2]) - set(color[n] for n in G[c])
        for i in available_colors:
            color[n] = i
            for n in G[c]:
                if color[n] == -1:
                    dfs(n)
            color[n] = -1

        if color.count(-1) == 0:
            print(c, color)
            nonlocal ans
            ans += 1
        for n in G[c]:
            if color[n] != -1:
                continue
            for i in available_colors:
                color[n] = i
                dfs(n)
                color[n] = -1

    dfs(0)

    print(ans)

if __name__ == '__main__':
    resolve()
