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
    H, W = LI()
    S = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    k = sum(i.count('#') for i in S)
    visited = [[False] * W for _ in range(H)]

    def dfs(cy, cx, ans):
        # print(cy, cx, ans, visited)
        ans.append((cy, cx))
        visited[cy][cx] = True
        if len(ans) == k:
            print(k)
            for i in ans:
                print(i[0] + 1, i[1] + 1)
            exit()
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '#' and not visited[ny][nx]:
                dfs(ny, nx, ans)
        ans.pop()
        visited[cy][cx] = False

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                dfs(i, j, [])

if __name__ == '__main__':
    resolve()
