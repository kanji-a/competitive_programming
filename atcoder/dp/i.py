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
    p = LF()

    # dp[i][j]: [0, i)のコインを投げたときj枚表が出る確率
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(i + 2):
            dp[i+1][j] = dp[i][j-1] * p[i] + dp[i][j] * (1 - p[i])
    # for i in dp:
    #     print(i)

    ans = sum(dp[-1][N//2+1:])
    print(ans)

if __name__ == '__main__':
    resolve()
