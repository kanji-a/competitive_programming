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
    N, Q = LI()
    A = LI()

    AA = []
    if A[0] != 1:
        AA.append(1)
    for i in range(N - 1):
        if A[i] + 1 != A[i+1]:
            AA.append(A[i] + 1)
    AA.append(A[-1] + 1)
    print(AA)

    index = [1]
    for i in range(len(AA) - 1):
        index.append(AA[i+1] - AA[i])
    print(index)

    for _ in range(Q):
        K = I()
        idx = bisect.bisect_left(index, K)
        # idx = bisect.bisect_right(index, K)
        print(idx)
        print(K + AA[idx] - index[idx])
        # print(K + AA[idx-1] - index[idx-1])



if __name__ == '__main__':
    resolve()
