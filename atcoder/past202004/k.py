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
    S = SS()
    C = LI()
    D = LI()

    # dp[i][j]: s[:i)の、カッコがj個開いた状態の最小コスト
    dp = [[INF] * N for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N):
            if S[i] == '(':
                if j + 1 < N:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1])
                if 0 <= j - 1:
                    dp[i+1][j-1] = min(dp[i][j] + C[i], dp[i+1][j-1])
            else:
                if 0 <= j - 1:
                    dp[i+1][j-1] = min(dp[i][j], dp[i+1][j-1])
                if j + 1 < N:
                    dp[i+1][j+1] = min(dp[i][j] + C[i], dp[i+1][j+1])
            dp[i+1][j] = min(dp[i][j] + D[i], dp[i+1][j])
    # for i in dp:
    #     print(i)

    print(dp[-1][0])

if __name__ == '__main__':
    resolve()

