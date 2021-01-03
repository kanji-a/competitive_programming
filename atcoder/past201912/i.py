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
    S = [0] * M
    C = [0] * M
    d = {'Y': '1', 'N': '0'}
    for i in range(M):
        s, c = LSS()
        S[i] = int(''.join([d[j] for j in s]), 2)
        C[i] = int(c)

    # dp[s]: 部品の集合sを得るための最小コスト
    dp = [INF] * 2 ** N
    dp[0] = 0

    for i in range(2 ** N):
        for j in range(M):
            dp[i | S[j]] = min(dp[i | S[j]], dp[i] + C[j])
    # print(dp)

    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])

if __name__ == '__main__':
    resolve()
