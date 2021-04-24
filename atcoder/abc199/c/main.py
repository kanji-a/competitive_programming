#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
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
    S = SS()
    Q = I()
    ans = list(S)

    is_flipped = False
    for _ in range(Q):
        T, A, B = LI()
        A -= 1
        B -= 1
        if T == 1:
            if is_flipped:
                if A >= N:
                    A -= N
                else:
                    A += N
                if B >= N:
                    B -= N
                else:
                    B += N
            ans[A], ans[B] = ans[B], ans[A]
        else:
            is_flipped = not is_flipped

    if is_flipped:
        ans = ans[N:] + ans[:N]

    print(''.join(ans))

if __name__ == '__main__':
    resolve()
