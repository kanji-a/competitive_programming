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
    H, W = LI()
    S = [SS() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    dp_acm_v = [[0] * (W + 1) for _ in range(H + 1)]
    dp_acm_v[1][1] = 1
    dp_acm_h = [[0] * (W + 1) for _ in range(H + 1)]
    dp_acm_h[1][1] = 1
    dp_acm_d = [[0] * (W + 1) for _ in range(H + 1)]
    dp_acm_d[1][1] = 1

    for i in range(H):
        for j in range(W):
            if i > 0 or j > 0:
                if S[i][j] == '.':
                    # 縦の累積和使用前
                    # tmp = 0
                    # for k in range(i + 1):
                    #     tmp += dp[k][j]
                    # dp[i][j] += tmp
                    dp[i][j] += dp_acm_v[i][j+1]
                    dp[i][j] += dp_acm_h[i+1][j]
                    dp[i][j] += dp_acm_d[i][j]
                    dp[i][j] %= MOD
                    dp_acm_v[i+1][j+1] = dp[i][j] + dp_acm_v[i][j+1]
                    dp_acm_v[i+1][j+1] %= MOD
                    dp_acm_h[i+1][j+1] = dp[i][j] + dp_acm_h[i+1][j]
                    dp_acm_h[i+1][j+1] %= MOD
                    dp_acm_d[i+1][j+1] = dp[i][j] + dp_acm_d[i][j]
                    dp_acm_d[i+1][j+1] %= MOD
    # for i in dp:
    #     print(i)
    # for i in dp_acm_v:
    #     print(i)
    # for i in dp_acm_h:
    #     print(i)
    # for i in dp_acm_d:
    #     print(i)

    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
