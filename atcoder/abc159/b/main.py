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
    N = len(S)

    ans = 'No'
    if S == S[::-1] and S[:(N-1)//2] == S[:(N-1)//2][::-1] and S[(N+3)//2-1:] == S[(N+3)//2-1:][::-1]:
        ans = 'Yes'
    
    print(ans)

if __name__ == '__main__':
    resolve()

