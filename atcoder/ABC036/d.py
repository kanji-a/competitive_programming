import bisect, collections, copy, functools, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
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
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    dp = [[1] * 2 for _ in range(N)]
    def f(c, p):
        for n in G[c]:
            if n != p:
                f(n, c)
                dp[c][0] *= (dp[n][0] + dp[n][1])
                dp[c][0] %= MOD
                dp[c][1] *= dp[n][0]
                dp[c][1] %= MOD

    f(0, -1)
    ans = dp[0][0] + dp[0][1]
    print(ans % MOD)

if __name__ == '__main__':
    resolve()
