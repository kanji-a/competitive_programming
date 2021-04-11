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
    S1 = SS()
    S2 = SS()
    S3 = SS()

    # 出現する文字は10種類以下
    chars = tuple(sorted(set(list(S1) + list(S2) + list(S3))))
    # print(chars)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return
    
    # 文字に対応する数字を決めて、好きが成り立つかチェック
    for i in itertools.permutations(range(10), len(chars)):
        d = {chars[j]: e for j, e in enumerate(i)}
        if d[S1[0]] == 0 or d[S2[0]] == 0 or d[S3[0]] == 0:
            continue
        N1 = 0
        for j, e in enumerate(S1[::-1]):
            N1 += d[e] * 10 ** j
        N2 = 0
        for j, e in enumerate(S2[::-1]):
            N2 += d[e] * 10 ** j
        N3 = 0
        for j, e in enumerate(S3[::-1]):
            N3 += d[e] * 10 ** j
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    
    print('UNSOLVABLE')

if __name__ == '__main__':
    resolve()
