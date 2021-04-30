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
    N, M = LI()
    ABC = [LI_() for _ in range(M)]

    ans = 0
    for i in range(2 ** N):
        s = set()
        for j in range(M):
            contain = [i >> k & 1 for k in ABC[j]]
            if contain.count(True) == 3:
                break
            elif contain.count(True) == 2:
                s.add(ABC[j][contain.index(False)])
        ans = max(len(s), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
