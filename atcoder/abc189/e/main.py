#!/usr/bin/env pypy
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

def matMul(A, B):
    A_h = len(A)
    B_h = len(B)
    B_w = len(B[0])
    C = [[0] * B_w for _ in range(A_h)]
    for i in range(A_h):
        for j in range(B_w):
            for k in range(B_h):
                C[i][j] += A[i][k] * B[k][j]
    return C

def resolve():
    N = I()
    XY = [LI() for _ in range(N)]
    # 変換回数ごとの累積変換を求めておく
    M = I()
    mat_acm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] * (M + 1)
    mat_acm[0] = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(M):
        op = LI()
        if op[0] == 1:
            mat = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
        elif op[0] == 2:
            mat = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        elif op[0] == 3:
            mat = [[-1, 0, 2 * op[1]], [0, 1, 0], [0, 0, 1]]
        else:
            mat = [[1, 0, 0], [0, -1, 2 * op[1]], [0, 0, 1]]
        mat_acm[i+1] = matMul(mat, mat_acm[i])
    # for i in mat_acm:
    #     print(i)

    Q = I()
    for _ in range(Q):
        A, B = LI()
        B -= 1
        ans = matMul(mat_acm[A], [[XY[B][0]], [XY[B][1]], [1]])
        print(ans[0][0], ans[1][0])

if __name__ == '__main__':
    resolve()
