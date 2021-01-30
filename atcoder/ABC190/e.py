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
        A, B = LI()
        G[A].append(B)
        G[B].append(A)
    K = I()
    C = LI()

    # TSP的な問題
    # 頂点C同士の距離をBFSで求める
    dist = {i: {j: INF for j in C} for i in C}
    for i in C:
        dist[i][i] = 0
    for i in C:
        d = [INF] * (N + 1)
        d[i] = 0
        que = collections.deque()
        que.append(i)
        while que:
            c = que.popleft()
            for n in G[c]:
                if d[n] == INF:
                    que.append(n)
                    d[n] = d[c] + 1
        for j in C:
            dist[i][j] = d[j]
    # print(dist)

    # dp[i][j]: 頂点集合iを通って最後にjにいる場合の最小距離
    dp = [{i: INF for i in C} for _ in range(2 ** K)]
    for i in C:
        dp[0][i] = 0
    for i in range(2 ** K):
        for j in C:
            # dp[i][j]から配る
            for k in range(K):
                if i >> k & 1 == 0:
                    nxt = i | 1 << k
                    dp[nxt][C[k]] = min(dp[i][j] + dist[j][C[k]], dp[nxt][C[k]])
    # print(dp)

    ans = min(dp[-1][i] for i in C) + 1
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    resolve()
