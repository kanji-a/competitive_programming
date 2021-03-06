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
    G = collections.defaultdict(list)
    for _ in range(M):
        X, Y, _ = LI_()
        G[X].append(Y)
        G[Y].append(X)

    # A_XtoA_Yは片方が決まればもう片方も決まる よって連結成分数が答え
    visited = [False] * N
    def dfs(c):
        visited[c] = True
        for n in G[c]:
            if not visited[n]:
                dfs(n)

    ans = [0]
    for i in range(N):
        if not visited[i]:
            dfs(i)
            ans[0] += 1

    print(ans[0])

if __name__ == '__main__':
    resolve()
