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
    H, N = LI()
    AB = [LI() for _ in range(N)]

    # dp[i]: モンスターの体力がiのときの消耗する魔力の最小値
    dp = [INF] * (H + 1)
    dp[0] = 0

    for i in range(1, H + 1):
        for a, b in AB:
                dp[i] = min(dp[max(i-a, 0)] + b, dp[i])

    print(dp[-1])

if __name__ == '__main__':
    resolve()
