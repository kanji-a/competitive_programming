import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    while True:
        w, h = LI()
        if w==0 and h==0:
            break
        else:
            # 縦と横の壁を別の配列に入れる
            wall_h = []
            wall_v = []
            for i in range(h-1):
                wall_v.append(LI())
                wall_h.append(LI())
            wall_v.append(LI())
            # print('wall_v')
            # for i in wall_v:
            #     print(i)
            # print('wall_h')
            # for i in wall_h:
            #     print(i)

            que = collections.deque()
            que.append((0, 0))
            dist = [[INF]*w for _ in range(h)]
            dist[0][0] = 1
            while que:
                cy, cx = que.popleft()
                # 右
                ny = cy
                nx = cx+1
                if 0<=ny<h and 0<=nx<w and wall_v[cy][cx]==0 and dist[ny][nx]>=INF:
                    que.append((ny, nx))
                    dist[ny][nx] = dist[cy][cx]+1
                # 下
                ny = cy+1
                nx = cx
                if 0<=ny<h and 0<=nx<w and wall_h[cy][cx]==0 and dist[ny][nx]>=INF:
                    que.append((ny, nx))
                    dist[ny][nx] = dist[cy][cx]+1
                # 左
                ny = cy
                nx = cx-1
                if 0<=ny<h and 0<=nx<w and wall_v[cy][cx-1]==0 and dist[ny][nx]>=INF:
                    que.append((ny, nx))
                    dist[ny][nx] = dist[cy][cx]+1
                # 上
                ny = cy-1
                nx = cx
                if 0<=ny<h and 0<=nx<w and wall_h[cy-1][cx]==0 and dist[ny][nx]>=INF:
                    que.append((ny, nx))
                    dist[ny][nx] = dist[cy][cx]+1

        # print(w, h, 'dist')
        # for i in dist:
        #     print(i)
        if dist[-1][-1]<INF:
            print(dist[-1][-1])
        else:
            print(0)
        


if __name__ == '__main__':
    resolve()