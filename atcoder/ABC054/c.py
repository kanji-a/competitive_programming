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

    ans = [0]
    visited = [False] * N
    def dfs(c, depth):
        visited[c] = True
        if depth == N - 1:
            ans[0] += 1
        else:
            for n in G[c]:
                if not visited[n]:
                    dfs(n, depth + 1)
                    visited[n] = False

    dfs(0, 0)

    print(ans[0])

if __name__ == '__main__':
    resolve()
