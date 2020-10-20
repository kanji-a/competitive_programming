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
    a = [SS() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if a[i][j] == '.':
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    # for i in dp:
    #     print(i)

    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
