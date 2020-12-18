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
    N, Q = LI()

    ans = [0] * N
    for _ in range(Q):
        L, R, T = LI()
        for i in range(L - 1, R):
            ans[i] = T

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
