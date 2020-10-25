import bisect, collections, copy, heapq, itertools, math, string, sys
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
    N, M = LI()
    X = LI()
    X = [[INF, X[0], X[1]], [X[0], INF, X[2]], [X[1], X[2], INF]]
    S = [ord(i) - ord('A') for i in SS()]
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B, C = LI()
        G[A-1].append((B - 1, C))
        G[B-1].append((A - 1, C))

    d_s = dijkstra(G, 0)
    d_g = dijkstra(G, N - 1)
    
    # 町1と町Nのワープ台タイプが同じ場合
    # 2段ワープ(XYX, XZX)か3段ワープ(XYZX, XZYX)か道で行く
    # 
    if S[0] == S[-1]:
        # 町1ともNとも違うワープタイプ
        r = [i for i in range(3) if i != S[0] and i != S[-1]]
        # 町1から一番近いr[0]の町までの距離
        s_r0 = INF
        if [d_s[i] for i in range(N) if S[i] == r[0]]:
            s_r0 = min([d_s[i] for i in range(N) if S[i] == r[0]])
        # 町Nから一番近いr[0]の町までの距離
        g_r0 = INF
        if [d_g[i] for i in range(N) if S[i] == r[0]]:
            g_r0 = min([d_g[i] for i in range(N) if S[i] == r[0]])
        # 町1から一番近いr[1]の町までの距離
        s_r1 = INF
        if [d_s[i] for i in range(N) if S[i] == r[1]]:
            s_r1 = min([d_s[i] for i in range(N) if S[i] == r[1]])
        # 町Nから一番近いr[1]の町までの距離
        g_r1 = INF
        if [d_g[i] for i in range(N) if S[i] == r[1]]:
            g_r1 = min([d_g[i] for i in range(N) if S[i] == r[1]])

        # ワープのみの場合(2段)
        ans = min(2 * X[S[0]][r[0]], 2 * X[S[0]][r[1]])
        # ワープのみの場合(3段)
        ans = min(X[S[0]][r[0]] + X[r[0]][r[1]] + X[r[1]][S[-1]], X[S[0]][r[1]] + X[r[1]][r[0]] + X[r[0]][S[-1]], ans)
        # 道のみの場合
        ans = min(d_s[-1], ans)
        # XYワープでYX道とXY道でYXワープ
        ans = min(X[S[0]][r[0]] + g_r0, s_r0 + X[r[0]][S[-1]], ans)
        # XZワープYX道とXZ道でZXワープ
        ans = min(X[S[0]][r[1]] + g_r1, s_r1 + X[r[1]][S[-1]], ans)
        # XYZワープでZX道とXY道でYZXワープ
        ans = min(X[S[0]][r[0]] + X[r[0]][r[1]] + g_r1, s_r0 + X[r[0]][r[1]] + X[r[1]][S[-1]], ans)
        # XZYワープでYX道とXZ道でZYXワープ
        ans = min(X[S[0]][r[1]] + X[r[1]][r[0]] + g_r0, s_r1 + X[r[1]][r[0]] + X[r[0]][S[-1]], ans)
    # 町1と町Nのワープ台タイプが違う場合
    else:
        # 町1ともNとも違うワープタイプ
        r = [i for i in range(3) if i != S[0] and i != S[-1]][0]
        # 町1から一番近いrの町までの距離
        s_r = min([d_s[i] for i in range(N) if S[i] == r])
        # 町Nから一番近いrの町までの距離
        g_r = min([d_g[i] for i in range(N) if S[i] == r])

        # ワープのみの場合
        ans = min(X[S[0]][S[-1]], X[S[0]][r] + X[r][S[-1]])
        # 道のみの場合
        ans = min(d_s[-1], ans)
        # XZワープでZY道とXZ道でZYワープ
        ans = min(X[S[0]][r] + g_r, s_r + X[r][S[-1]], ans)

    print(ans)

if __name__ == '__main__':
    resolve()
