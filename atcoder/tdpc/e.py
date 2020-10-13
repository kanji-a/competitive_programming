import bisect, collections, copy, heapq, functools, itertools, math, string, sys
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
    D = I()
    N = SS()

    len_N = len(N)

    # dp[i][j][k]: [0, i)桁目まで見た時, j:未満フラグ, k: modD
    dp = [[[0] * D for _ in range(2)] for _ in range(len_N + 1)]
    dp[0][0][0] = 1
    for i in range(len_N):
        N_i = int(N[i])
        for j in range(D):
            for k in range(10):
                dp[i+1][1][(j+k)%D] += dp[i][1][j]
                dp[i+1][1][(j+k)%D] %= MOD
            for k in range(N_i):
                dp[i+1][1][(j+k)%D] += dp[i][0][j]
                dp[i+1][1][(j+k)%D] %= MOD
            dp[i+1][0][(j+N_i)%D] += dp[i][0][j]
            dp[i+1][0][(j+N_i)%D] %= MOD
    # print(dp)

    print((dp[-1][0][0] + dp[-1][1][0] - 1) % MOD)
    
if __name__ == '__main__':
    resolve()
