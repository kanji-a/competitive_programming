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
    G = collections.defaultdict(set)
    for _ in range(M):
        A, B = LI_()
        G[A].add(B)
        G[B].add(A)
    # print(G)

    # 連結成分をすべてバラバラにできればよい→最大の連結成分がわかればよい
    visited = [False] * N
    def dfs(c, cnt):
        visited[c] = True
        cnt[0] += 1
        for n in G[c]:
            if not visited[n]:
                dfs(n, cnt)

    ans = 0
    for i in range(N):
        cnt = [0]
        dfs(i, cnt)
        ans = max(cnt[0], ans)

    print(ans)

if __name__ == '__main__':
    resolve()
