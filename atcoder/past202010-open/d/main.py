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
    S = SS()

    # 最左#より左の.の数だけAが必要、最右#より右の.の数だけBが必要
    # それで埋まらなかった.の数だけAかBをやればよい
    ans = [0, 0]
    cnt = [len(i) for i in S.split('#')]
    # print(cnt)
    ans[0] = cnt[0]
    ans[1] = cnt[-1]
    if len(cnt) >= 3:
        max_blank = max(cnt[1:-1])
        ans[0] += max(max_blank - sum(ans), 0)

    print(*ans)

if __name__ == '__main__':
    resolve()
