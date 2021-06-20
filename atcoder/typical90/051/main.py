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
    N, K, P = LI()
    A = LI()

    N_half = N // 2
    A_f = A[:N_half]
    A_s = A[N_half:]

    AA_f = []
    for i in range(2 ** N_half):
        tmp = 0
        cnt = 0
        for j in range(N_half):
            if i >> j & 1:
                tmp += A_f[j]
                cnt += 1
        AA_f.append((cnt, tmp))
    AA_s = []
    for i in range(2 ** (N - N_half)):
        tmp = 0
        cnt = 0
        for j in range(N - N_half):
            if i >> j & 1:
                tmp += A_s[j]
                cnt += 1
        AA_s.append((cnt, tmp))
    AA_s.sort()
    # print(AA_f)
    # print(AA_s)

    ans = 0
    for c, i in AA_f:
        # 個数があっていて値段がPより大きい一番左のインデックス - 個数があっている一番左のインデックス
        idx_l = bisect.bisect_right(AA_s, (K - c, -1))
        idx_r = bisect.bisect_right(AA_s, (K - c, P - i))
        # print(idx_l, idx_r)
        ans += idx_r - idx_l

    print(ans)

if __name__ == '__main__':
    resolve()
