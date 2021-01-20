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
    # 座標圧縮2次元累積和
    # ではなく平面走査法というものらしい
    d = {}
    for _ in range(Q):
        x, y, D, C = LI()

    for _ in range(Q):
        A, B = LI()

if __name__ == '__main__':
    resolve()
