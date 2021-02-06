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
    N, M = LI()
    s = [SS() for _ in range(N)]

    ans = [[-1] * M for _ in range(N)]

    for i, j in itertools.product(range(N), range(M)):
        cnt = 0
        for k, l in itertools.product(range(-1, 2), repeat=2):
            if 0 <= i + k < N and 0 <= j + l < M and s[i+k][j+l] == '#':
                cnt += 1
        ans[i][j] = str(cnt)

    for i in ans:
        print(''.join(i))

if __name__ == '__main__':
    resolve()
