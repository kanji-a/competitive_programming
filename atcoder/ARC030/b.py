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
    n, x = LI()
    x -= 1
    h = LI()
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    print(G)

    def dfs(c, p):
        if h[c] == 1:
            print(c)
        for n in G[c]:
            if n != p:
                dfs(n, c)

    dfs(x, -1)

if __name__ == '__main__':
    resolve()
