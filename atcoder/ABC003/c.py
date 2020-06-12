import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    c = [list(input().split()) for _ in range(R)]

    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dist = [[float('inf')]*C for _ in range(R)]

    que = deque()
    que.append(((sy-1, sx-1), 0, set()))
    while len(que)>0:
        now = que.popleft()
        dist[now[0][0]][now[0][1]] = min(now[1], dist[now[0][0]][now[0][1]])
        for d in dir:
            next = (now[0][0]+d[0], now[0][1]+d[1])
            print(next)
            if 0<=next[0]<R and 0<=next[1]<C and c[next[0]][next[1]]=='.' and not next in now[2]:
                que.append((next, now[1]+1, now[2]|{now[0]}))

    print(dist[gy-1][gx-1])

if __name__ == '__main__':
    resolve()
