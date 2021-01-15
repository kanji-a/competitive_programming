import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    G = collections.defaultdict(list)
    for _ in range(M):
        X, Y = LI_()
        G[X].append(Y)

    # dp[i]: iに到達可能なiより前の頂点での最安値
    dp = [INF] * N

    for c in range(N):
        for n in G[c]:
            dp[n] = min(dp[c], A[c], dp[n])

    # print(dp)

    ans = max([a - d for d, a in zip(dp, A)])
    print(ans)

if __name__ == '__main__':
    resolve()
