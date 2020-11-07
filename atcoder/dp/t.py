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
    s = SS()

    # [0, i)までみたとき、一番右の数より大きいものがj個残っている場合の数
    dp = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        if s[i] == '<':
            for j in range(N):
                dp[i+1][j] = 

if __name__ == '__main__':
    resolve()
