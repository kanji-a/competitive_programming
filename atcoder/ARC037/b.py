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
        u, v = LI_()
        G[u].append(v)
        G[v].append(u)

    def dfs(c, visited):
        for n in G[c]:
            if n not in visited:
                visited.add(n)
                dfs(n, visited)

    V = []
    visited = set()
    for i in range(N):
        # 連結成分の頂点を集める
        if i not in visited:
            tmp = {i}
            dfs(i, tmp)
            visited |= tmp
            V.append(tmp)

    # 連結成分の頂点数と変数の比較
    ans = 0
    for i in V:
        if sum([len(G[j]) for j in i]) == 2 * (len(i) - 1):
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
