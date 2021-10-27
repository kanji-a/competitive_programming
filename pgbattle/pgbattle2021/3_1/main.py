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

    # 引用元 https://www.geeksforgeeks.org/count-digits-factorial-set-1/
    def findDigits(n):
        
        # factorial exists only for n>=0
        if (n < 0):
            return 0;
    
        # base case
        if (n <= 1):
            return 1;
    
        # else iterate through n and
        # calculate the value
        digits = 0;
        for i in range(2, n + 1):
            digits += math.log10(i);
    
        return math.floor(digits) + 1;

    ans = findDigits(N)
    print(ans)

if __name__ == '__main__':
    resolve()
