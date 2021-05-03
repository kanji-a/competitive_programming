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
    r, c = LI_()
    s = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    panel = ('^', '<', 'v', '>')
    ans = [[j if j == '#' else 'x' for j in i] for i in s]
    deq = collections.deque()
    deq.append((r, c))

    while deq:
        cy, cx = deq.pop()
        ans[cy][cx] = 'o'
        for i in range(4):
            dy, dx = d[i]
            p = panel[i]
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and s[ny][nx] in (p, '.') and ans[ny][nx] == 'x':
                deq.append((ny, nx))

    for i in ans:
        print(''.join(i))

if __name__ == '__main__':
    resolve()
