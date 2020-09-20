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
    c = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    s = ()
    g = ()
    for i in range(H):
        for j in range(W):
            if c[i][j] == 's':
                s = (i, j)
            if c[i][j] == 'g':
                g = (i, j)

    que = collections.deque([s])
    dist = [[INF] * W for _ in range(H)]
    dist[s[0]][s[1]] = 0
    while que:
        cy, cx = que.popleft()
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if c[ny][nx] == '#':
                    if dist[ny][nx] > dist[cy][cx] + 1:
                        dist[ny][nx] = dist[cy][cx] + 1
                        que.append((ny, nx))
                else:
                    if dist[ny][nx] > dist[cy][cx]:
                        dist[ny][nx] = dist[cy][cx]
                        que.appendleft((ny, nx))
                    
    # for i in dist:
    #     print(i)
    if dist[g[0]][g[1]] <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    resolve()
