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

    ans = 'Yes'
    len_S = len(S)
    for i in range(len_S):
        if i % 2 == 0 and S[i] in string.ascii_uppercase or i % 2 == 1 and S[i] in string.ascii_lowercase:
            ans = 'No'

    print(ans)

if __name__ == '__main__':
    resolve()
