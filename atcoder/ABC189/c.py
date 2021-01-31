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
    A = LI()

    acm_min = [INF] * (N + 1)
    for i in range(N):
        acm_min[i+1] = min(A[i], acm_min[i])
    print(A, acm_min)

    ans = 0
    for l in range(N):
        r = bisect.bisect_right(acm_min, A[l])
        ans = max(A[i] * (r - l - 1), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
