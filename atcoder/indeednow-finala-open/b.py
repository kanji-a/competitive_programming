import bisect, collections, copy, heapq, itertools, math, string, sys
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
    R, C = LI()
    a = [SS() for _ in range(R)]
    dir = (((0, 1), (-1 , 0), (-1, -1), (0, -1), (1, -1), (1, 0)), ((0, 1), (-1 , 1), (-1, 0), (0, -1), (1, 0), (1, 1)))

    sy, sx, ty, tx = -1, -1, -1, -1
    for i, j in itertools.product(range(R), range(C)):
        if a[i][j] == 's':
            sy = i
            sx = j
        if a[i][j] == 't':
            ty = i
            tx = j

    que = []
    d = [[INF] * C for _ in range(R)]
    d[sy][sx] = 0
    heapq.heappush(que, (d[sy][sx], (sy, sx)))

    while que:
        p = heapq.heappop(que)
        cy, cx = p[1]
        if d[cy][cx] < p[0]: continue
        for dy, dx in dir[cy%2]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < R and 0 <= nx < C:
                a_num = int(a[ny][nx]) if a[ny][nx] in '0123456789' else 0
                if d[ny][nx] > d[cy][cx] + a_num:
                    d[ny][nx] = d[cy][cx] + a_num
                    heapq.heappush(que, (d[ny][nx], (ny, nx)))

    ans = d[ty][tx]
    print(ans)
    # for i in d:
    #     print(i)

if __name__ == '__main__':
    resolve()
