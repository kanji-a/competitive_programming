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
    N = I()
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if N == 0:
        print(0)
        return

    ans_r = []
    while N:
        ans_r.append(s[N % 36])
        N //= 36 

    print(''.join(ans_r[::-1]))

if __name__ == '__main__':
    resolve()
