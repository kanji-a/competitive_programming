#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    A, B, C, K = LI()

    if A+B>=K:
        print(min(A, K))
    else:
        print(A-(K-(A+B)))

if __name__ == '__main__':
    resolve()
