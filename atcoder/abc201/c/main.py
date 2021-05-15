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

def comb(n, r):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i)
        denom = denom * i
    return numer // denom
    
def resolve():
    S = SS()

    cnt = collections.Counter(S)
    # oの数字を使う箇所を確保して、
    if cnt['o'] > 4:
        print(0)
        return
    ans = comb(4, cnt['o']) * math.factorial(cnt['o']) * math.factorial(cnt['?']) // math.factorial(cnt['?'] - (4 - cnt['o']))
    print(ans)

if __name__ == '__main__':
    resolve()
