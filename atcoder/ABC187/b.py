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
    N = I()
    xy = [LI() for _ in range(N)]

    ans = 0
    for xy0, xy1 in itertools.combinations(xy, 2):
        if xy0[0] > xy1[0]:
            xy0, xy1 = xy1, xy0
        x0, y0 = xy0
        x1, y1 = xy1
        if -(x1 - x0) <= y1 - y0 <= x1 - x0:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
