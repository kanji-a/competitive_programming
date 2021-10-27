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
    N, S = LI()
    d = LI()

    cnt = collections.Counter(d)
    # aで実現可能なSの範囲
    S_max = sum((10 ** k - 1) * v for k, v in cnt.items())
    S_min = sum(10 ** (k - 1) * v for k, v in cnt.items())

    # 範囲外の場合は作れない
    if S < S_min or S_max < S:
        print(-1)
        sys.exit()

    # 範囲に入っていれば必ず作れる

    # 各a_iには事前に最小値を設定しておき、前から順に和がSになるよう数字を増やしていく
    a = [10 ** (i - 1) for i in d]
    S -= S_min
    for i in range(N):
        m = 10 ** d[i] - 1
        # print(S, m, i)
        if S >= m - a[i]:
            S -= m - a[i]
            a[i] = m
        else:
            a[i] += S
            break

    print(*a)

if __name__ == '__main__':
    resolve()
