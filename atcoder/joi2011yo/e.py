import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    H, W, N = map(int, input().split())
    c = [input() for _ in range(H)]

    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    point = [()]*(N+1)
    for i in range(H):
        for j in range(W):
            if c[i][j]=='S':
                point[0] = (i, j)
            elif c[i][j]!='X' and c[i][j]!='.':
                point[int(c[i][j])] = (i, j)

    ans = 0
    for i in range(N):
        que = deque()
        dist = [[-1]*W for _ in range(H)]
        que.append(point[i])
        dist[point[i][0]][point[i][1]] = 0

        while len(que)>0:
            now_y, now_x = que.popleft()
            if now_y==point[i+1][0] and now_x==point[i+1][1]:
                break
            for dy, dx in dir:
                next_y = now_y+dy
                next_x = now_x+dx
                if 0<=next_y<H and 0<=next_x<W and c[next_y][next_x]!='X' and dist[next_y][next_x]==-1:
                    que.append((next_y, next_x))
                    dist[next_y][next_x] = dist[now_y][now_x]+1

        ans += dist[point[i+1][0]][point[i+1][1]]

    print(ans)

if __name__ == '__main__':
    resolve()
