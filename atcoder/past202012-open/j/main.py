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
    S = SS()
    X = I() - 1

    # XをSのどれかのアルファベットを指すindexになるまで小さくしていく方針

    # Sの出力の長さ
    l = [0] * (len(S) + 1)
    for i in range(len(S)):
        if S[i] in string.ascii_lowercase:
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i] * (int(S[i]) + 1)
    # print(l)

    idx = len(S) - 1
    # print(idx)
    while 0 <= idx:
        if S[idx].isdigit() and l[idx] < X + 1:
            X %= l[idx]
        elif l[idx] == X:
            break
        idx -= 1
        # print(idx, X)

    print(S[X])

if __name__ == '__main__':
    resolve()
