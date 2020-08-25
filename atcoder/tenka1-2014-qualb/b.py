import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 1000000007
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

    T = [SS() for _ in range(N)]
    len_S = len(S)
    T_len = [len(i) for i in T]

    # dp[i]: S[0, i)を作れるフレーズ数
    dp = [0] * (len_S + 1)
    dp[0] = 1
    for i in range(1, len_S + 1):
        tmp = 0
        for j in range(N):
            if i - T_len[j] >= 0 and S[i-T_len[j]:i] == T[j]:
                tmp += dp[i-T_len[j]]
                tmp %= MOD
        dp[i] = tmp

    # print(dp)
    print(dp[-1])

if __name__ == '__main__':
    resolve()
