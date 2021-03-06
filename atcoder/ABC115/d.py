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
    N, X = LI()
    X -= 1

    # バーガーの厚さ
    l = [0] * (N + 1)
    l[0] = 1
    for i in range(N):
        l[i+1] = 2 * l[i] + 3

    # バーガーのパティ数
    p = [0] * (N + 1)
    p[0] = 1
    for i in range(N):
        p[i+1] = 2 * p[i] + 1

    def rec(n, x):
        if n == 0:
            return 1
        else:
            if x == 0:
                return 0
            elif 1 <= x <= l[n-1]:
                return rec(n - 1, x - 1)
            elif x == l[n-1] + 1:
                return p[n-1] + 1
            elif l[n-1] + 2 <= x <= l[n] - 2:
                return p[n-1] + 1 + rec(n - 1, x - 2 - l[n-1])
            elif x == l[n] - 1:
                return p[n]

    ans = rec(N, X)
    print(ans)

if __name__ == '__main__':
    resolve()
