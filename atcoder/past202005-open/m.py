import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
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
        u, v = LI_()
        G[u].append(v)
        G[v].append(u)
    s = I() - 1
    K = I()
    t = LI_()

    t_to_t = {j: {i: INF for i in t} for j in t}
    # 街t間の最小通行料をBFSで求める
    for i in t:
        que = collections.deque()
        que.append(i)
        dist = [INF] * N
        dist[i] = 0
        while que:
            c = que.popleft()
            for n in G[c]:
                if dist[n] == INF:
                    que.append(n)
                    dist[n] = dist[c] + 1
        for j in t:
            t_to_t[i][j] = min(dist[j], t_to_t[i][j])
    # print(d)

    # sから街tへの最短経路
    que = collections.deque()
    que.append(s)
    dist = [INF] * N
    dist[s] = 0
    while que:
        c = que.popleft()
        for n in G[c]:
            if dist[n] == INF:
                que.append(n)
                dist[n] = dist[c] + 1
    s_to_t = {i: dist[i] for i in t}
    # print(s_to_t)

    # d[i][j]: sスタートでiの街を回って最後がjの場合の最低通行料
    dp = [{i: INF for i in t} for _ in range(2 ** K)]
    for i, j in enumerate(t):
        dp[1>>i][j] = 0
    for i in range(2 ** K):
        for j in t:
            for k, l in enumerate(t):
                if not i >> k & 1:
                    n = i | 1 << k
                    # print(n)
                    dp[n][l] = min(dp[i][j] + t_to_t[j][l], dp[n][l])
    # print(dp)

    # 最後に終わりの街からsへの経路を足せば良い
    ans = min(dp[-1][i] + s_to_t[i] for i in t)
    print(ans)

if __name__ == '__main__':
    resolve()
