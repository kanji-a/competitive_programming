import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**6)

def resolve():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    cnt = [0]*N
    for i in range(Q):
        p, x = map(int, input().split())
        cnt[p-1] += x

    def dfs(v, par):
        if v>0:
            cnt[v] += cnt[par]
        for i in edge[v]:
            if i!=par:
                dfs(i, v)

    dfs(0, -1)

    print(*cnt)

if __name__ == '__main__':
    resolve()
