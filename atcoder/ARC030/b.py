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
    # print(G)

    # まず、通るべき頂点に印をつける
    to_go = [False] * n
    def dfs_to_go(c, p):
        if h[c] == 1:
            to_go[c] = True
        for n in G[c]:
            if n != p:
                dfs_to_go(n, c)
                if to_go[n]:
                    to_go[c] = True
    dfs_to_go(x, -1)
    # print(to_go)

    # 通るべき頂点を通った距離を求める
    ans = [0]
    def dfs_ans(c, p):
        for n in G[c]:
            if n != p and to_go[n]:
                ans[0] += 1
                dfs_ans(n, c)
                ans[0] += 1
    dfs_ans(x, -1)
    print(ans[0])

if __name__ == '__main__':
    resolve()
