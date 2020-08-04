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
    x, y = LI()
    N = I()
    xy = [LI() for _ in range(N)]

    ans = INF
    for i in range(N):
        x0, y0 = xy[i]
        x1, y1 = xy[(i+1)%N]
        s = ((x0 - x) * (y1 - y) - (x1 - x) * (y0 - y)) / 2
        l = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        ans = min(2 * s / l, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
