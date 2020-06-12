import sys, collections, itertools
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
# INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    W, H = LI()
    area = []
    # 外を0で囲う
    area.append([0]*(W+2))
    for _ in range(H):
        area.append([0]+LI()+[0])
    area.append([0]*(W+2))

    # BFSで内外判定
    d_hex = (((0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)), ((0, 1), (-1, 1), (-1, 0), (0, -1), (1, 0), (1, 1)))
    d_hex_r = (((0, 1), (-1, 0), (1, 0)), ((0, 1), (-1, 1), (1, 1)))
    que = collections.deque()
    que.append((0, 0))
    dist = [[INF]*(W+2) for _ in range(H+2)]
    dist[0][0] = 0
    while que:
        cy, cx = que.popleft()
        for dy, dx in d_hex[cy%2]:
            ny = cy+dy
            nx = cx+dx
            if 0<=ny<H+2 and 0<=nx<W+2 and area[ny][nx]==0 and dist[ny][nx]>=INF:
                que.append((ny, nx))
                dist[ny][nx] = dist[cy][cx]+1
    # print('dist')
    # for i in dist:
    #     print(i)

    # セルの右上、右、右下が境界であれば加算
    ans = 0
    for y, x in itertools.product(range(H+2), range(W+2)):
        tmp = 0
        for dy, dx in d_hex_r[y%2]:
            ny = y+dy
            nx = x+dx
            if 0<=ny<H+2 and 0<=nx<W+2 and (dist[y][x]<INF)!=(dist[ny][nx]<INF):
                ans += 1
                tmp += 1
    print(ans)

if __name__ == '__main__':
    resolve()
