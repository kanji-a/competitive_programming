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
    N = I()
    A = [LI() for _ in range(N)]
    ave = [sum(i) / 6 for i in A]
    ave.append(INF)
    min_A = min([min(i) for i in A])

    # dp[i]: iを出した後に振る回数の期待値
    dp = collections.defaultdict(INF)
    dp[min_A] = 0
    # サイコロの出目は単調減少

if __name__ == '__main__':
    resolve()
