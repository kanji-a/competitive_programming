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

def dijkstra(G, H, W, s):
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    que = []
    dist = [[INF] * W for _ in range(H)]
    dist[s[0]][s[1]] = 0
    heapq.heappush(que, (dist[s[0]][s[1]], s))

    while que:
        p = heapq.heappop(que)
        cy, cx = p[1]
        if dist[cy][cx] < p[0]: continue
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] > dist[cy][cx] + G[ny][nx]:
                dist[ny][nx] = dist[cy][cx] + G[ny][nx]
                heapq.heappush(que, (dist[ny][nx], (ny, nx)))
    return dist

def resolve():
    H, W = LI()
    A = [LI() for _ in range(H)]

    # ある点Xを決めて、左下→X→右下→X→右上というルートを考える
    # Xが右下の点でもよい

    # 事前計算
    dist_dl = dijkstra(A, H, W, (H - 1, 0))
    dist_dr = dijkstra(A, H, W, (H - 1, W - 1))
    dist_ur = dijkstra(A, H, W, (0, W - 1))

    ans = INF
    for i, j in itertools.product(range(H), range(W)):
        ans = min(dist_dl[i][j] + dist_dr[i][j] + dist_ur[i][j] - 2 * A[i][j], ans)

    print(ans)

if __name__ == '__main__':
    resolve()
