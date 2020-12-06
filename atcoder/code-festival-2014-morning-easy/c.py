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

def dijkstra(G, s, n):
    que = []
    d = [INF]*n
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))
    return d

def resolve():
    n, m = LI()
    s, t = LI_()
    G = collections.defaultdict(list)
    for _ in range(m):
        x, y, d = LI()
        G[x-1].append((y - 1, d))
        G[y-1].append((x - 1, d))

    dist_s = dijkstra(G, s, n)
    dist_t = dijkstra(G, t, n)

    # 連結グラフとは限らないので、到達不能点はuにはならない
    ans = [i + 1 for i in range(n) if dist_s[i] == dist_t[i] and dist_s[i] < INF and dist_t[i] < INF]
    if ans:
        print(ans[0])
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
