import sys, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def dijkstra(G, s):
    que = []
    d = [INF]*len(G)
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
    n, k = LI()
    G = [[] for _ in range(n)]
    for _ in range(k):
        q = LI()
        if q[0]==0:
            a = q[1]-1
            b = q[2]-1
            d = dijkstra(G, a)
            if d[b]<INF:
                print(d[b])
            else:
                print(-1)
        else:
            c = q[1]-1
            d = q[2]-1
            e = q[3]
            G[c].append([d, e])
            G[d].append([c, e])
            # print(G)
    
if __name__ == '__main__':
    resolve()
