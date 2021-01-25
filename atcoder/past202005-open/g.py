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
    N, X, Y = LI()
    obstacle = set()
    for _ in range(N):
        x, y = LI()
        obstacle.add((y, x))
    d = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0))

    que = collections.deque()
    que.append((0, 0))
    dist = {(0, 0): 0}
    while que:
        cy, cx = que.popleft()
        if cy == Y and cx == X:
            break
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            # 障害物とゴールがありうる領域の外側ギリギリを通れるようにする
            if -201 <= ny <= 201 and -201 <= nx <= 201 and (ny, nx) not in obstacle and (ny, nx) not in dist:
                que.append((ny, nx))
                dist[(ny, nx)] = dist[(cy, cx)] + 1
    # print(dist)

    if (Y, X) in dist:
        print(dist[(Y, X)])
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
