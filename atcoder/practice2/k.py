import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
import atcoder.lazysegtree as lazysegtree
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
    a = LI()

    lst = lazysegtree.LazySegTree()

if __name__ == '__main__':
    resolve()
