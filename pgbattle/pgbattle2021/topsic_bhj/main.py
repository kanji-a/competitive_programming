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
    N, S = LI()
    d = LI()

    # 小さい桁数の方から限界まで大きく使ってSを減らしていく

    cnt = collections.Counter(d)
    # d_idx[i]: 値がiになっている箇所のインデックス
    d_idx = [[] for _ in range(10)]
    for i in range(N):
        d_idx[d[i]].append(i)

    # ans_pre[i]: i桁の数の合計
    ans_pre = [0] * 10
    is_ok = True
    for i in range(1, 10):
        # その桁数*個数で表せる最大の数
        lim_max = (10 ** i - 1) * cnt[i]
        lim_min = (10 ** (i - 1)) * cnt[i]
        if lim_min <= S <= lim_max:
            ans_pre[i] = S
            S = 0
            break
        elif S > lim_max:
            ans_pre[i] = lim_max
            S -= lim_max
        else:
            is_ok = False

    if is_ok and S == 0:
        # print(ans_pre)
        a = [0] * N
        for i in range(1, 10):
            n = 10 ** i - 1
            q = ans_pre[i] // n
            r = ans_pre[i] % n
            for j in range(q):
                a[d_idx[i][j]] = n
            if q < len(d_idx[i]):
                a[d_idx[i][-1]] = r
        print(* a)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
