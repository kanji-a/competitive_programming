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
    A = LI()
    B = LI()

    # 編集距離
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = i
    for i in range(M + 1):
        dp[0][i] = i

    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i+1][j] + 1, dp[i][j+1] + 1, dp[i][j] + 1)
    # for i in dp:
    #     print(i)

    ans = dp[-1][-1]
    print(ans)

if __name__ == '__main__':
    resolve()
