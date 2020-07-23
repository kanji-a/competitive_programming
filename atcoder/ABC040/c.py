import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    a = LI()

    dp = [0] * (N)
    dp[1] = abs(a[1] - a[0])

    for i in range(N - 2):
        dp[i+2] = min(dp[i] + abs(a[i+2] - a[i]), dp[i+1] + abs(a[i+2] - a[i+1]))

    print(dp[-1])

if __name__ == '__main__':
    resolve()
