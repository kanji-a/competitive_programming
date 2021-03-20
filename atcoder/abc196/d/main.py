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
    H, W, A, B = LI()

    ans = 0
    used = [[False] * W for _ in range(H)]
    
    def dfs(yx, a, b):
        if yx == H * W:
            nonlocal ans
            ans += 1
            return
        y = yx // W
        x = yx % W
        if used[y][x]:
            dfs(yx + 1, a, b)
            return
        # 1x1
        if b > 0:
            used[y][x] = True
            dfs(yx + 1, a, b - 1)
            used[y][x] = False
        if a > 0:
            # 縦向き
            if y + 1 < H and not used[y+1][x]:
                used[y][x] = True
                used[y+1][x] = True
                dfs(yx + 1, a - 1, b)
                used[y][x] = False
                used[y+1][x] = False
            # 横向き
            if x + 1 < W and not used[y][x+1]:
                used[y][x] = True
                used[y][x+1] = True
                dfs(yx + 1, a - 1, b)
                used[y][x] = False
                used[y][x+1] = False

    dfs(0, A, B)

    print(ans)

if __name__ == '__main__':
    resolve()
