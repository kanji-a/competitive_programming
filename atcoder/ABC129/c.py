import bisect, collections, copy, heapq, itertools, math, string, sys
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
    N, M = LI()
    a = set([I() for _ in range(M)])

    dp = [0] * (N + 1)
    dp[0] = 1
    if 1 not in a:
        dp[1] = 1
    for i in range(N - 1):
        if i + 2 not in a:
            dp[i+2] = dp[i] + dp[i+1]
            dp[i+2] %= MOD

    print(dp[-1])

if __name__ == '__main__':
    resolve()
