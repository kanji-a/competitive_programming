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
    W, H, N = LI()
    l = 0
    r = W
    u = H
    d = 0
    for _ in range(N):
        x, y, a = LI()
        if a == 1:
            l = max(x, l)
        elif a == 2:
            r = min(x, r)
        elif a == 3:
            d = max(y, d)
        else:
            u = min(y, u)
    ans = max(r - l, 0) * max(u - d, 0)
    print(ans)

if __name__ == '__main__':
    resolve()
