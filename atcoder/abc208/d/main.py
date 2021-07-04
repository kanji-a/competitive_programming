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
        A, B, C = LI()
        A -= 1
        B -= 1
        G[A].append((B, C))

    # s,t間のmaxがわかればよい
    # max_on_path = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     dist[i][i] = 0
        # max_on_path[i][i] = -1

    ans = 0

    def bfs(i, k):
        dist = [[0] * N for _ in range(N)]
        que = collections.deque([i])
        while que:
            c = que.popleft()
            for n, d in G[c]:
                if dist[i][n] == 0:
                    dist[i][n] = dist[i][c] + d
                    if n <= k:
                        que.append(n)
        print(i, k)
        for j in dist:
            print(j)
        nonlocal ans
        ans += sum(dist[i])

    for i in range(N):
        for k in range(N):
            bfs(i, k)
    # for i in dist:
    #     print(i)
    # for i in max_on_path:
    #     print(i)
    print(ans)

if __name__ == '__main__':
    resolve()
