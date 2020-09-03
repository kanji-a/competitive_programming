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
    N = I()
    xy = [LI() for _ in range(N)]

    ans = 0
    for p0, p1, p2 in itertools.combinations(xy, 3):
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = p2
        v0 = (x1 - x0, y1 - y0)
        v1 = (x2 - x0, y2 - y0)
        s = abs(v0[0] * v1[1] - v0[1] * v1[0])
        if s >= 2 and s % 2 == 0:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
