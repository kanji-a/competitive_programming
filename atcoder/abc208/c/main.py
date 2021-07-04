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
    N, K = LI()
    a = LI()

    num = K // N 
    r = K % N
    s = set(i[0] for i in sorted(enumerate(a), key=lambda x: x[1])[:r])
    # print(s)
    
    for i in range(N):
        if i in s:
            print(num + 1)
        else:
            print(num)

if __name__ == '__main__':
    resolve()
