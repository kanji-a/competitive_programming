import sys, collections, bisect, itertools, heapq, math, copy
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
    N, W = LI()
    vwm = [LI() for _ in range(N)]

    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(0, N):
        for j in range(0, W+1):
            v = vwm[i][0]
            w = vwm[i][1]
            m = vwm[i][2]
            dp[i+1][j] = dp[i][j]
            k = 0
            while k <= m and w * k <= j:
                dp[i+1][j] = max(dp[i][j-w*k]+v*k, dp[i+1][j])
                k += 1

    # for i in dp:
    #     print(i)
    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
