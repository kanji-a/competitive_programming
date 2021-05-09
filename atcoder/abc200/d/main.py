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
    A = LI()

    # Bを全パターン作っていては間に合わない
    # BとCのあまりを決め打ち?
    # BとCの共通部分は意味ないので、BとCは被らないものだけ探せば良い
    ans = [[] for _ in range(200)]
    for i in range(2 ** N):
        tmp_ans = []
        tmp_sum = 0
        for j in range(N):
            if i >> j & 1:
                tmp_ans.append(j)
                tmp_sum += A[j]
                tmp_sum %= 200
        ans[tmp_sum].append(tmp_ans)

    for i in ans:
        if len(i) >= 2:
            print(i)

if __name__ == '__main__':
    resolve()
