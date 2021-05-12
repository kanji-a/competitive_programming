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

def matMulMod(A, B, l, m, n):
    A_h = len(A)
    B_h = len(B)
    B_w = len(B[0])
    C = [[0] * n for _ in range(l)]
    for i in range(l):
        for j in range(n):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= MOD
    return C

def matPowMod(A, s, n):
    B = [[int(i == j) for j in range(s)] for i in range(s)]
    while n > 0:
        if n & 1:
            B = matMulMod(B, A, s, s, s)
        A = matMulMod(A, A, s, s, s)
        n >>= 1
    return B
    
def resolve():
    N, B, K = LI()
    c = LI()

    tmp = [[0] for _ in range(B)]
    tmp[0][0] = 1

    mat = [[0] * B for _ in range(B)]
    for i in range(B):
        for j in c:
            mat[i][(i*10+j)%B] += 1
    # for i in mat:
    #     print(i)

    matpow = matPowMod(mat, B, N)
    prod = matMulMod(matpow, tmp, B, B, 1)

    print(prod[0][0])

if __name__ == '__main__':
    resolve()
