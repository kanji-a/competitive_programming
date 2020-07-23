import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    S = SS()

    def lcs(s0, s1):
        n, m = len(s0), len(s1)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s0[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    # LCSを全ての分割に対して求めれば良い
    ans = N
    for i in range(N - 1):
        s0 = S[:i+1]
        s1 = S[i+1:]
        ans = min(N - 2 * lcs(s0, s1), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
