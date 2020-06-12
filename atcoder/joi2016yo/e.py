import sys, heapq, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
# INF = 10**5
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def dijkstra_(G, s, C, dangerous_city, P, Q):
    que = []
    d = [INF]*len(G)
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if not e[0] in C:
                if e[0] in dangerous_city:
                    cost = Q
                else:
                    cost = P
                if d[e[0]] > d[v] + cost:
                    d[e[0]] = d[v] + cost
                    heapq.heappush(que, (d[e[0]], e[0]))
    return d

def resolve():
    N, M, K, S = LI()
    P, Q = LI()
    C = [I()-1 for _ in range(K)]
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = LI_()
        G[A].append([B, 1])
        G[B].append([A, 1])

    # BFSで危険な街を出す
    dangerous_city = set()
    for i in C:
        dist = [INF]*N
        dist[i] = 0
        deq = collections.deque()
        deq.append(i)
        while deq:
            city_c = deq.popleft()
            if dist[city_c]==S:
                break
            for city_n, _ in G[city_c]:
                if dist[city_n]>=INF:
                    dist[city_n] = dist[city_c] + 1
                    deq.append(city_n)
                    dangerous_city.add(city_n)

    # コストを行き先の街の宿代になるようにしてダイクストラ
    min_cost = dijkstra_(G, 0, C, dangerous_city, P, Q)
    if N-1 in dangerous_city:
        print(min_cost[N-1]-Q)
    else:
        print(min_cost[N-1]-P)

if __name__ == '__main__':
    resolve()
