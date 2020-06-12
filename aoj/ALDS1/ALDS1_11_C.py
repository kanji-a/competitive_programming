import sys
input = lambda: sys.stdin.readline().rstrip() 
from collections import deque

def resolve():
    n = int(input())
    ukv = [list(map(int, input().split())) for _ in range(n)]

    dist = [-1]*n
    que = deque()

    que.append(0)
    dist[0] = 0
    while len(que)>0:
        v = que.popleft()
        for i in ukv[v][2:]:
            if dist[i-1]==-1:
                que.append(i-1)
                dist[i-1] = dist[v]+1

    for i in range(n):
        print(i+1, dist[i])

if __name__ == '__main__':
    resolve()