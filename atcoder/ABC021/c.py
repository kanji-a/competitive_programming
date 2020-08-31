import sys, collections, functools, itertools
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
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
    G = collections.defaultdict(list)
    for _ in range(M):
        x, y = LI_()
        G[x].append(y)
        G[y].append(x)
    # print(G)

    deq = collections.deque([a])
    dist = [INF] * N
    dist[a] = 0
 
    # 頂点毎の最短距離を探索する
    while deq:
        c = deq.popleft()
        for n in G[c]:
            if dist[n] == INF:
                deq.append(n) 
                dist[n] = dist[c] + 1

    # cからbへの経路数
    @functools.lru_cache
    def dfs(c):
        if c == b:
            return 1
        else:
            ret = 0
            for n in G[c]:
                if dist[n] == dist[c] + 1:
                    ret += dfs(n)
                    ret %= MOD
            return ret

    ans = dfs(a)
    print(ans)

if __name__ == '__main__':
    resolve()
