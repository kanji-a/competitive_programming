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
    C = LI()
    G = collections.defaultdict(list)
    for _ in range(N - 1):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    d = collections.defaultdict(int)
    ans = []
    
    def dfs(c, p):
        # print(c, C[c], d)
        if d[C[c]] == 0:
            ans.append(c)
        d[C[c]] += 1
        for n in G[c]:
            if n != p:
                dfs(n, c)
        d[C[c]] -= 1
    
    dfs(0, -1)

    for i in sorted(ans):
        print(i + 1)

if __name__ == '__main__':
    resolve()
