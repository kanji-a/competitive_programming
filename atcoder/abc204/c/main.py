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

    ans = 0
    for i in range(N):
        que = collections.deque()
        que.append(i)
        visited = [False] * N
        visited[i] = True
        while que:
            c = que.popleft()
            ans += 1
            for n in G[c]:
                if visited[n]:
                    continue
                que.append(n)
                visited[n] = True

    print(ans)

if __name__ == '__main__':
    resolve()
