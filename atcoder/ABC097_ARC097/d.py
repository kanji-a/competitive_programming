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
    p = LI_()
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = LI_()
        G[x].append(y)
        G[y].append(x)
    # print(G)

    visited = [False] * N
    def dfs(c, tmp):
        visited[c] = True
        tmp.append(c)
        for n in G[c]:
            if not visited[n]:
                dfs(n, tmp)

    # 連結成分内はswapで自由な位置に移動可能
    c = []
    for i in range(N):
        if not visited[i]:
            tmp = []
            dfs(i, tmp)
            c.append(tmp)
    # print(c)

    ans = sum([len({p[j] for j in i} & set(i)) for i in c])
    print(ans)

if __name__ == '__main__':
    resolve()
