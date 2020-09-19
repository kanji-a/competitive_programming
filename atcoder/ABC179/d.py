import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    LR = [LI() for _ in range(K)]

    # N * KのDP?
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for l, r in LR:
            for j in range(i + l, min(i + r + 1, N)):
                dp[j] += dp[i]
                dp[j] %= MOD

    print(dp[-1])

if __name__ == '__main__':
    resolve()
