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
    AB = [LI() for _ in range(N)]
    
    time_acm = [0] * (N + 1)
    for i in range(N):
        A, B = AB[i]
        time_acm[i+1] = time_acm[i] + A / B
    # print(time_acm)

    half = time_acm[-1] / 2

    idx = bisect.bisect_left(time_acm, half)
    # print(idx)
    ans = sum([i for i, _ in AB][:idx-1]) + (half - time_acm[idx-1]) * AB[idx-1][1]
    print(ans)

if __name__ == '__main__':
    resolve()
