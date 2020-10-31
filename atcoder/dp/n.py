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
    acm_a = list(itertools.accumulate(a, initial=0))
    # print('acm',acm_a)

    # dp[i][j]: a[i, j)のスライムを1匹にするのに必要な最小コスト
    dp = [[0] * (N + 1) for _ in range(N)]
    for i in range(N):
        for j in range(i + 2, N + 1):
            dp[i][j] = INF

    # この順番でやらないと決まってない値を使ってしまう
    for i in range(N - 2, -1, -1):
        for j in range(i + 2, N + 1):
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][k] + dp[k][j] + (acm_a[j] - acm_a[i]), dp[i][j])
    # for i in dp:
    #     print(i)

    print(dp[0][-1])

if __name__ == '__main__':
    resolve()
