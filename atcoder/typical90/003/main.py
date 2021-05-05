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
    G = collections.defaultdict(list)
    for _ in range(N - 1):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    d1 = [-1] * N
    d1[0] = 0
    que1 = collections.deque()
    que1.append(0)
    while que1:
        c = que1.pop()
        for n in G[c]:
            if d1[n] == -1:
                que1.appendleft(n)
                d1[n] = d1[c] + 1
    # print(d1)
    v = d1.index(max(d1))

    d2 = [-1] * N
    d2[v] = 0
    que2 = collections.deque()
    que2.append(v)
    while que2:
        c = que2.pop()
        for n in G[c]:
            if d2[n] == -1:
                que2.appendleft(n)
                d2[n] = d2[c] + 1
    # print(d2)

    print(max(d2) + 1)

if __name__ == '__main__':
    resolve()
