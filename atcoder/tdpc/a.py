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
    p = LI()

    sum_p = sum(p)
    dp = [[False] * (sum_p + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(sum_p + 1):
            dp[i][j] = dp[i-1][j]
            if j - p[i-1] >= 0:
                dp[i][j] = dp[i][j] or dp[i-1][j-p[i-1]]
    # for i in dp:
    #     print(i)

    ans = dp[-1].count(True)
    print(ans)

if __name__ == '__main__':
    resolve()
