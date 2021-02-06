#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
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
    aa = a * 2
    aa_acm = list(itertools.accumulate(aa, initial=0))
    sum_a = sum(a)

    ans = INF
    # 始点を決めて終点を2分探索
    for i in range(N):
        idx = bisect.bisect_left(aa_acm, aa_acm[i] + sum_a // 2)
        X = aa_acm[idx] - aa_acm[i]
        Y = sum_a - X
        X_ = aa_acm[idx-1] - aa_acm[i]
        Y_ = sum_a - X_
        ans = min(abs(X - Y), abs(X_ - Y_) ,ans)

    print(ans)

if __name__ == '__main__':
    resolve()

