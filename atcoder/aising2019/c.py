import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    S = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(cy, cx, cnt):
        visited[cy][cx] = True
        if S[cy][cx] == '#':
            cnt[0] += 1
        else:
            cnt[1] += 1
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and S[ny][nx] != S[cy][cx]:
                dfs(ny, nx, cnt)

    # (黒マス数, 白マス数)
    c = []
    visited = [[False] * W for _ in range(H)]
    for i, j in itertools.product(range(H), range(W)):
        if not visited[i][j]:
            cnt = [0, 0]
            dfs(i, j, cnt)
            c.append(cnt)

    ans = sum([b * w for b, w in c])
    print(ans)

if __name__ == '__main__':
    resolve()
