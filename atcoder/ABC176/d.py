import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    Ch, Cw = LI_()
    Dh, Dw = LI_()
    S = [list(SS()) for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1)) 

    que = collections.deque()
    que.append(Ch, Cw, 0)
    S[Ch][Cw] = 0
    while que:
        cy, cx, cost = que.popleft()
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.':
                S[ny][nx] = cost
                que.append((ny, nx, cost))

if __name__ == '__main__':
    resolve()
