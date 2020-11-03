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
    h = LI()
    a = LI()

    # dp[i]: 列の長さiの一番右の高さの最小値
    dp = [INF] * N
    for i in range(N):
        dp[bisect.bisect_left(dp, h[i])] = h[i]
    return bisect.bisect_left(dp, INF)

if __name__ == '__main__':
    resolve()
