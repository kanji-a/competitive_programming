import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    c = [input() for _ in range(R)]

    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dist = [[-1]*C for _ in range(R)]

    que = deque()
    que.append((sy-1, sx-1))
    dist[sy-1][sx-1] = 0
    while len(que)>0:
        now_y, now_x = que.popleft()
        if now_y==gy-1 and now_x==gx-1:
            break
        for dy, dx in dir:
            next_y = now_y+dy
            next_x = now_x+dx
            if c[next_y][next_x]=='.' and dist[next_y][next_x]==-1:
                que.append((next_y, next_x))
                dist[next_y][next_x] = dist[now_y][now_x]+1

    print(dist[gy-1][gx-1])

if __name__ == '__main__':
    resolve()
