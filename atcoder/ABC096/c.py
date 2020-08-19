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
    s = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(cy, cx, tmp):
        tmp.append((cy, cx))
        visited[cy][cx] = True
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and s[ny][nx] == '#' and not visited[ny][nx]:
                dfs(ny, nx, tmp)

    # 大きさ1の#の島があったらダメ
    is_ok = True
    visited = [[False] * W for _ in range(H)]
    for i, j in itertools.product(range(H), range(W)):
        if s[i][j] == '#' and not visited[i][j]:
            tmp = []
            dfs(i, j, tmp)
            if len(tmp) == 1:
                is_ok = False
                break

    if is_ok:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
