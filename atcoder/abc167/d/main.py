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
    N, K = LI()
    A = LI_()

    log_K = 1
    while 1 << log_K <= K:
        log_K += 1

    # doubling[i][j]: 街jから2^i進んだ街
    doubling = [[0] * N for _ in range(log_K)]
    for i in range(N):
        doubling[0][i] = A[i]

    for i in range(log_K - 1):
        for j in range(N):
            doubling[i+1][j] = doubling[i][doubling[i][j]]
    # for i in doubling:
    #     print(i)
    
    ans = 0
    i = 0
    while K >> i > 0:
        if K >> i & 1:
            ans = doubling[i][ans]  
        i += 1

    print(ans + 1)

if __name__ == '__main__':
    resolve()
