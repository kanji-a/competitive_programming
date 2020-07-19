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
    for i, j in itertools.combinations(range(N), 2):
        x_i = xy[i][0]
        y_i = xy[i][1]
        x_j = xy[j][0]
        y_j = xy[j][1]
        ans = max(((x_i - x_j) ** 2 + (y_i - y_j) ** 2) ** 0.5, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
