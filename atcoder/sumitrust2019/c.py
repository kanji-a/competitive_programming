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
    X = I()

    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(1, X + 1):
        for j in range(100, 106):
            if i - j >= 0:
                dp[i] |= dp[i-j]
    # print(dp)

    if dp[X]:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    resolve()
