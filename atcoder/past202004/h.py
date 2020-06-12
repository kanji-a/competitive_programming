import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]

    S = ()
    G = ()
    for i in range(N):
        for j in range(M):
            if A[i][j]=='S':
                S = (i, j)
            elif A[i][j]=='G':
                G = (i, j)

    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ans = 0
    for i in range(1, 11):
        que = deque()
        dist = [[-1]*M for _ in range(N)]
        dist[point[i][0]][point[i][1]] = 0

        while len(que)>0:
            now_y, now_x = que.popleft()
            if i==10:
                if A[now_y][now_x]=='G':
                    ans += dist[now_y][now_x]
                    break
            else:
                if A[now_y][now_x]==str(i):
                    ans += dist[now_y][now_x]
                    break
            for dy, dx in dir:
                next_y = now_y+dy
                next_x = now_x+dx
                if 0<=next_y<N and 0<=next_x<M and dist[next_y][next_x]==-1:
                    que.append((next_y, next_x))
                    dist[next_y][next_x] = dist[now_y][now_x]+1


    print(ans)
if __name__ == '__main__':
    resolve()
