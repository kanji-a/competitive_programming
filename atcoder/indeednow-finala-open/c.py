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
    N, M = LI()
    m = 100
    # クエリが多いので、事前に計算を終わらせておく
    # その能力を持っている人が得られる最大年収
    dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)]
    for _ in range(N):
        a, b, c, w = LI()
        # 要求能力が同じなら、最大の年収のところ以外は無意味
        dp[a][b][c] = max(w, dp[a][b][c])

    for i in range(m + 1):
        for j in range(m + 1):
            for k in range(m + 1):
                if i - 1 >= 0:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j][k])
                if j - 1 >= 0:
                    dp[i][j][k] = max(dp[i][j-1][k], dp[i][j][k])
                if k - 1 >= 0:
                    dp[i][j][k] = max(dp[i][j][k-1], dp[i][j][k])

    for _ in range(M):
        x, y, z = LI()
        print(dp[x][y][z])

    # for i in dp:
    #     for j in i:
    #         print(j)
    #     print('---')

if __name__ == '__main__':
    resolve()
