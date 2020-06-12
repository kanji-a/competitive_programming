import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    a, b = LI_()
    M = I()
    con = [[False]*N for _ in range(N)]
    for i in range(M):
        xy = LI_()
        con[xy[0]][xy[1]] = True
        con[xy[1]][xy[0]] = True

    ans = [0]
    deq = collections.deque()
    deq.append(a)
    dist = [INF]*N
    dist[a] = 0

    while len(deq)>0:
        city_c = deq.popleft()
        for city_n in range(N):
            if con[city_c][city_n] and dist[city_n]>=INF:
                deq.append(city_n) 
                dist[city_n] = dist[city_c]+1
    
    dist_city = [[] for _ in range(100)]
    for i, e in enumerate(dist):
        dist_city[e].append(i)

    def dfs(city_c, depth):
        if city_c==b:
            ans[0] += 1
        else:
            for city_n in dist_city[depth+1]:
                if con[city_c][city_n]:
                    dfs(city_n, depth+1)

    dfs(a, 0)
    print(ans[0])

if __name__ == '__main__':
    resolve()
