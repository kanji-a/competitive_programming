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
    A, B, C = LI()
    
    abs_A = abs(A)
    abs_B = abs(B)

    if A >= 0 and B >= 0:
        if A < B:
            print('<')
        elif A > B:
            print('>')
        else:
            print('=')
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if A < B:
                print('>')
            elif A > B:
                print('<')
            else:
                print('=')
        else:
            if A < B:
                print('<')
            elif A > B:
                print('>')
            else:
                print('=')
    elif A >= 0 and B < 0:
        if C % 2 == 0:
            if abs_A > abs_B:
                print('>')
            elif abs_A < abs_B:
                print('<')
            else:
                print('=')
        else:
            print('>')
    elif A < 0 and B >= 0:
        if C % 2 == 0:
            if abs_A > abs_B:
                print('>')
            elif abs_A < abs_B:
                print('<')
            else:
                print('=')
        else:
            print('<')

if __name__ == '__main__':
    resolve()
