import bisect, collections, copy, functools, heapq, itertools, math, string, sys
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
    a = [LI() for _ in range(N)]

    # dp = [0] * 2 ** N
    # dp[0] = 1

    # s: 集合
    @functools.lru_cache
    def rec(s):
        print(s, bin(s))
        if s == 0:
            return 1
        res = 0
        for i in range(N):
            if s >> i & 1:
                if a[i][i] == 1:
                    res += rec(s - (1 << i))
                    res %= MOD
        return res

    ans = rec(2 ** N - 1)
    print(ans)

if __name__ == '__main__':
    resolve()
