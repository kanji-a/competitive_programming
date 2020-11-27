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
    n = I()
    slp = [LI() for _ in range(n)]
    m = I()
    w = [I() for _ in range(m)]
    max_w = max(w)

    dp = [0] * (max_w + 1)
    for i in range(1, max_w + 1):
        for s, l, p in slp:
            for j in range(s, l + 1):
                if i - j >= 0:
                    dp[i] = max(dp[i-j] + p, dp[i])

    ans = [dp[i] for i in w]
    if 0 in ans:
        print(-1)
    else:
        for i in ans:
            print(i)

if __name__ == '__main__':
    resolve()