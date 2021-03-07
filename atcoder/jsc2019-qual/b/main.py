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
    A = LI()

    # A内の転倒数
    inv_num_in = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                inv_num_in += 1
                inv_num_in %= MOD
    # print(inv_num_in)

    # 異なるA間の転倒数
    inv_num_out = 0
    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                inv_num_out += 1
                inv_num_out %= MOD
    # print(inv_num_out)

    ans = (inv_num_in * K % MOD + inv_num_out * K * (K - 1) // 2 % MOD) % MOD
    print(ans)

if __name__ == '__main__':
    resolve()
