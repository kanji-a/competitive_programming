import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    H, W = map(int, input().split())
    s = []
    white_num = 0
    for i in range(H):
        s.append(input())
        white_num += s[i].count('.')

    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dist = [[-1]*W for _ in range(H)]
    que = deque()
    que.append((0, 0))
    dist[0][0] = 0

    while len(que)>0:
        now_y, now_x = que.popleft()
        if now_y==H-1 and now_x==W-1:
            break
        for dy, dx in dir:
            next_y = now_y+dy
            next_x = now_x+dx
            if 0<=next_y<H and 0<=next_x<W and s[next_y][next_x]=='.' and dist[next_y][next_x]==-1:
                que.append((next_y, next_x))
                dist[next_y][next_x] = dist[now_y][now_x] + 1

    if dist[H-1][W-1]==-1:
        print(-1)
    else:
        print(white_num-(dist[H-1][W-1]+1))

if __name__ == '__main__':
    resolve()
