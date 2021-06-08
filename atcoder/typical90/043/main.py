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
    H, W = LI()
    rs, cs = LI_()
    rt, ct = LI_()
    S = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # 01BFS
    # そのマスに進入した方向 ↓→↑←の順
    dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
    for i in range(4):
        dist[rs][cs][i] = 0
    que = collections.deque()
    que.append((rs, cs))

    while que:
        cy, cx = que.popleft()
        for i in range(4):
            dy, dx = d[i]
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.':
                for j in range(4):
                    if i == j:
                        if dist[ny][nx][i] > dist[cy][cx][j]:
                            dist[ny][nx][i] = dist[cy][cx][j]
                            que.appendleft((ny, nx))
                    else:
                        if dist[ny][nx][i] > dist[cy][cx][j] + 1:
                            dist[ny][nx][i] = dist[cy][cx][j] + 1
                            que.append((ny, nx))
    # for i in dist:
    #     print(i)

    ans = min(dist[rt][ct])
    print(ans)

if __name__ == '__main__':
    resolve()
