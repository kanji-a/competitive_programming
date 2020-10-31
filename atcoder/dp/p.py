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
    G = collections.defaultdict(list)
    for _ in range(N - 1):
        x, y = LI_()
        G[x].append(y)
        G[y].append(x)

    # dp[i][j]: 頂点i以下で頂点iが色jの場合の場合の数
    # j: 0:白、1:黒
    dp = [[1] * 2 for _ in range(N)]

    def rec(c, p):
        for n in G[c]:
            if n != p:
                rec(n, c)
                # cが白の場合
                dp[c][0] *= dp[n][0] + dp[n][1]
                dp[c][0] %= MOD
                # cが黒の場合
                dp[c][1] *= dp[n][0]
                dp[c][1] %= MOD

    rec(0, -1)

    ans = (dp[0][0] + dp[0][1]) % MOD
    print(ans)

if __name__ == '__main__':
    resolve()
