import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
from atcoder.fenwicktree import FenwickTree
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
    n = I()
    A = LI()
    sorted_A = sorted(A)
    d = {}
    for i, e in enumerate(sorted_A):
        d[e] = i

    fwt = FenwickTree(n)
    ans = 0
    for i, e in enumerate(A):
        fwt.add(d[e], 1)
        ans += i - fwt.sum(0, d[e])

    print(ans)

if __name__ == '__main__':
    resolve()
