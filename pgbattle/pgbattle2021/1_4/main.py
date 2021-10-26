#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
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
    N = I()
    A = LI()
    S = LI()
    S_acm = list(itertools.accumulate(S, initial=0))
    # print(S_acm)

    ans = 0
    s = set()
    right = 0
    for left in range(N):
        while right < N and A[right] not in s:
            s.add(A[right])
            right += 1
        # print(left, right, s)
        ans += S_acm[right-left]
        ans %= MOD

        if right == left:
            right += 1
        else:
            s.discard(A[left])

    print(ans)

if __name__ == '__main__':
    resolve()
