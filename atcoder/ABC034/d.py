import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, K = LI()
    wp = [LI() for _ in range(N)]

    # p_sum = sum([i[1] for i in wp])
    # # dp[i][j]: [0,i)から3つ使って作れる食塩jはった食塩水の
    # dp = [[0]*p_sum for _ in range(N+1)]

    # for i in range(N):
    #     for j in range(p_sum):
    #         if j-wp[i+1][1]>=0:
    #             dp[i+1][j] = max(dp[i][j-wp[i+1][1]]+1, dp[i+1][j])

if __name__ == '__main__':
    resolve()