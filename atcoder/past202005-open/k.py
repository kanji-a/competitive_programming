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

    # 1-indexed
    # 自分の下のコンテナの番号 机はナンバー*(-1)
    ptr = [-i for i in range(N + 1)]
    # 机の一番上のコンテナの番号
    top = [i for i in range(N + 1)]

    for _ in range(Q):
        f, t, x = LI()
        top[f], ptr[x], top[t] = ptr[x], top[t], top[f]

    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        c = top[i]
        while c > 0:
            ans[c] = i
            c = ptr[c]

    for i in range(1, N + 1):
        print(ans[i])

if __name__ == '__main__':
    resolve()
