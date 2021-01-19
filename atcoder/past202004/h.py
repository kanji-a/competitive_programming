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

def resolve():
    N, M = LI()
    A = [SS() for _ in range(N)]

    c = [[] for _ in range(11)]
    for i in range(N):
        for j in range(M):
            a = A[i][j]
            if a == 'S':
                c[0].append((i, j))
            elif a == 'G':
                c[10].append((i, j))
            else:
                c[int(a)].append((i, j))
    # print(c)

    que = []
    d = [[INF] * M for _ in range(N)]
    d[c[0][0][0]][c[0][0][1]] = 0
    heapq.heappush(que, (0, c[0][0], 0))

    while que:
        num, xy, dist = heapq.heappop(que)
        cy, cx = xy
        if d[cy][cx] < dist or num == 10: continue
        for e in c[num+1]:
            ny, nx = e
            nd = d[cy][cx] + (abs(ny - cy) + abs(nx - cx))
            if d[ny][nx] > nd:
                d[ny][nx] = nd
                heapq.heappush(que, (num + 1, (ny, nx), nd))
    
    ans = d[c[-1][0][0]][c[-1][0][1]]
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    resolve()

