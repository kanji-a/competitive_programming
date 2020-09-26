import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 100000
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    w, h = LI()

    # dp[i][j][k][l]: kは2本前の方向、lは1本前の方向
    # 方向 0: 右、1: 上
    dp = [[[[0] * 2 for _ in range(2)] for _ in range(w)] for _ in range(h)]
    for i in range(1, h):
        dp[i][0][1][1] = 1
    for i in range(1, w):
        dp[0][i][0][0] = 1

    for i in range(1, h):
        for j in range(1, w):
            dp[i][j][0][0] = (dp[i][j-1][0][0] + dp[i][j-1][1][0]) % MOD
            dp[i][j][0][1] = dp[i-1][j][0][0]
            dp[i][j][1][0] = dp[i][j-1][1][1]
            dp[i][j][1][1] = (dp[i-1][j][1][1] + dp[i-1][j][0][1]) % MOD
    # for i in dp:
    #     print(i)

    ans = sum([sum(i) for i in dp[-1][-1]]) % MOD
    print(ans)

if __name__ == '__main__':
    resolve()
