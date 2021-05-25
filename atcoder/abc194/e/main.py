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
    N, M = LI()
    A = LI()

    cnt = [0] * (max(A) + 2)
    for i in range(M):
        cnt[A[i]] += 1
    # print(cnt)
    ans = 0
    for i in range(len(cnt)):
        if cnt[i] == 0:
            ans = i
            break

    for i in range(N - M):
        cnt[A[i]] -= 1
        cnt[A[i+M]] += 1
        if A[i] < ans and cnt[A[i]] == 0:
            ans = A[i]

    print(ans)

if __name__ == '__main__':
    resolve()
