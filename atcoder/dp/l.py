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
    a = LI()

    # dp[i][j]: a[i, j)のX-Yの値
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    # dp[k][k+1]=0 を基底としてdp[0][N]を目指すので逆順ループ
    for i in range(N, -1, -1):
        for j in range(i + 1, N + 1):
            # 先手のターン
            if (N - (j - i)) % 2 == 0:
                dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j-1] + a[j-1])
            # 後手のターン
            else:
                dp[i][j] = min(dp[i+1][j] - a[i], dp[i][j-1] - a[j-1])
    # for i in dp:
    #     print(i)

    print(dp[0][-1])

if __name__ == '__main__':
    resolve()
