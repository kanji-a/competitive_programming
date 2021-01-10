import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    A = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        X, Y = LI_()
        G[X].append(Y)

    visited = [False] * N
    ans = [-INF]
    
    def dfs(c, m):
        # print(c, m, A[c])
        visited[c] = True
        for n in G[c]:
            ans[0] = max(A[n] - m, ans[0])
            dfs(n, min(A[n], m))

    for i in range(N):
        if not visited[i] and G[i]:
            dfs(i, A[i])

    print(ans[0])

if __name__ == '__main__':
    resolve()
