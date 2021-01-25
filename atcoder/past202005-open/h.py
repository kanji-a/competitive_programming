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
    N, L = LI()
    x = set(LI())
    T = LI()

    dp = [INF] * (L + 1)
    dp[0] = 0
    for i in range(L):
        a = T[2] if i in x else 0
        if i + 1 <= L:
            dp[i+1] = min(dp[i] + T[0] + a, dp[i+1])
        if i + 2 <= L:
            dp[i+2] = min(dp[i] + T[0] // 2 + a + T[1] + T[0] // 2, dp[i+2])
        if i + 4 <= L:
            dp[i+4] = min(dp[i] + T[0] // 2 + a + T[1] * 3 + T[0] // 2, dp[i+4])
    ans = dp[-1]

    # ジャンプで通過する場合
    for i in range(1, 4):
        ans = min(dp[L-i] + T[0] // 2 + (T[2] if L - i in x else 0) + T[1] * (i * 2 - 1) // 2, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
