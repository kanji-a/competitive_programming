import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n, k = LI()

    if n <= k:
        ans = 1
        for i in range(n):
            ans *= (k - i)
            ans %= MOD
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    resolve()
