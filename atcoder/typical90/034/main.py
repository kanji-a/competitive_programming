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
    N, K = LI()
    a = LI()

    ans = 0
    r = 0
    cnt = collections.Counter()
    len_cnt = 0
    for l in range(N):
        while r < N and (len_cnt < K or len_cnt == K and cnt[a[r]] > 0):
            # print(l, r, cnt)
            if cnt[a[r]] == 0:
                len_cnt += 1
            cnt[a[r]] += 1
            r += 1
        ans = max(r - l, ans)
        if r == l:
            r += 1
        else:
            if cnt[a[l]] == 1:
                len_cnt -= 1
            if cnt[a[l]] > 0:
                cnt[a[l]] -= 1


    print(ans)

if __name__ == '__main__':
    resolve()
