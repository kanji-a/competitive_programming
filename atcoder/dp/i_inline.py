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
    p = LF()

    # dp[j]: j枚表が出る確率
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(N):
        for j in range(i + 1, -1, -1):
            dp[j] = dp[j-1] * p[i] + dp[j] * (1 - p[i])
    # for i in dp:
    #     print(i)

    ans = sum(dp[N//2+1:])
    print(ans)

if __name__ == '__main__':
    resolve()
