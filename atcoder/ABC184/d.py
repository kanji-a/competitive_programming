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
    A, B, C = LI()

    lim = 100
    # lim = 3
    dp = [[[-1] * (lim + 1) for _ in range(lim + 1)] for _ in range(lim + 1)]
    for i, j, k in itertools.product(range(lim + 1), repeat=3):
        if lim in (i, j, k):
            dp[i][j][k] = 0

    for i in range(lim - 1, -1, -1):
        for j in range(lim - 1, -1, -1):
            for k in range(lim - 1, -1, -1):
                if i + j + k > 0:
                    dp[i][j][k] = dp[i+1][j][k] * i / (i + j + k) + dp[i][j+1][k] * j / (i + j + k) + dp[i][j][k+1] * k / (i + j + k) + 1

    # for i in dp:
    #     print(i)
    print(dp[A][B][C])

if __name__ == '__main__':
    resolve()
