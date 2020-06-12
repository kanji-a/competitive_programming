import sys, heapq, collections
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

def dijkstra_(G, s, CR):
    que = []
    d = [INF]*len(G)
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e] > d[v] + CR[v][0]:
                d[e] = d[v] + CR[v][0]
                heapq.heappush(que, (d[e], e))
    return d

def resolve():
    N, K = LI()
    CR = [LI() for _ in range(N)]
    G = [[] for _ in range(N)]
    for _ in range(K):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    # その街からのタクシーで行ける街をBFSで求めて辺を張る
    G_taxi = [[] for _ in range(N)]
    for i in range(N):
        deq = collections.deque()
        deq.append(i)
        dist = [INF]*N
        dist[i] = 0
        while deq:
            city_c = deq.popleft()
            if dist[city_c] >= CR[i][1]:
                break
            for city_n in G[city_c]:
                if dist[city_n]>=INF:
                    deq.append(city_n)
                    dist[city_n] = dist[city_c] + 1
                    G_taxi[i].append(city_n)
    # print(G_taxi)

    min_cost = dijkstra_(G_taxi, 0, CR)
    print(min_cost[-1])

if __name__ == '__main__':
    resolve()