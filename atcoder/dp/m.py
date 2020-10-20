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
    N, K = LI()
    a = LI()

    # dp[i][j]: [0, i)で残りj個
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    sdp = [[0] * (K + 2) for _ in range(N + 1)]
    dp[0][-1] = 1
    sdp[0][-1] = 1

    for i in range(N):
        for j in range(K + 1):
            # ↓を累積和で高速化 累積和は貰うDPで書く
            # for k in range(a[i] + 1):
            #     if j + k < K + 1:
            #         dp[i+1][j] += dp[i][j+k]

            # ↑を参考に累積和に書き直し
            dp[i+1][j] += sdp[i][min(j+a[i]+1, K+1)] - sdp[i][j]
            dp[i+1][j] %= MOD
            # ↑で更新した値を使って累積和の方も更新
            sdp[i+1][j+1] = sdp[i+1][j] + dp[i+1][j]
            sdp[i+1][j+1] %= MOD
    # for i in dp:
    #     print(i)
    # for i in sdp:
    #     print(i)

    ans = dp[-1][0]
    print(ans)

if __name__ == '__main__':
    resolve()
