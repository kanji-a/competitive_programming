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
    G = collections.defaultdict(list)
    for _ in range(M):
        x, y = LI_()
        G[x].append(y)

    # dp[i]: 頂点iからの最長パスの距離
    dp = [0] * N

    def f(c):
        if dp[c] == 0:
            for n in G[c]:
                dp[c] = max(f(n) + 1, dp[c])
        return dp[c]

    for i in range(N):
        f(i)

    # print(dp)
    print(max(dp))

if __name__ == '__main__':
    resolve()
