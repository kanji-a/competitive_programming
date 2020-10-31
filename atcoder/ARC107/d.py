import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()

    def f(n, k, num):
        if n == 0:
            return 1
        else:
            for i in range(num, N + 1):
                return f(n - 1, k - 2 ** (-i), i)

if __name__ == '__main__':
    resolve()
