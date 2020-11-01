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
    N = I()
    xy = [LI() for _ in range(N)]

    ans = 'No'
    for i, j, k in itertools.combinations(range(N), 3):
        x0, y0 = xy[i]
        x1, y1 = xy[j]
        x2, y2 = xy[k]
        if (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0):
            ans = 'Yes'
            break

    print(ans)

if __name__ == '__main__':
    resolve()
