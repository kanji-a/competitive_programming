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
    A, B, C = LI()
    A %= 10

    if A in (1, 5, 6):
        print(A)
    elif A in (4, 9):
        if B % 2 == 0:
            print(A ** 2 % 10)
        else:
            print(A)
    else:
        # B ** Cを4で割った余り
        r = pow(B, C, 4)
        if r == 0:
            r = 4
        print(A ** r % 10)
    
if __name__ == '__main__':
    resolve()
