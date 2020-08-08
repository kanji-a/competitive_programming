import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    cnt = [0]
    visited = [False] * N

    def dfs(c):
        visited[c] = True
        for n in G[c]:
            if not visited[n]:
                dfs(n)

    for i in range(N):
        if not visited[i]:
            cnt[0] += 1
            dfs(i)

    print(cnt[0] - 1)

if __name__ == '__main__':
    resolve()
