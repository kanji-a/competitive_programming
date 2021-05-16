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
    S = SS()

    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        cnt = collections.Counter(num)
        is_ok = True
        for j, e in enumerate(S):
            if e == 'o' and cnt[str(j)] == 0 or e == 'x' and cnt[str(j)] >= 1:
                is_ok = False
        if is_ok:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
