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
    N, M, Q = LI()
    solve = [[0] * M for _ in range(N)]
    point = [N] * M
    for _ in range(Q):
        s = LI()
        if s[0] == 1:
            n = s[1] - 1
            print(sum(solve[n][i] * point[i] for i in range(M)))
        else:
            n, m = s[1:]
            n -= 1
            m -= 1
            point[m] -= 1
            solve[n][m] = 1

if __name__ == '__main__':
    resolve()
