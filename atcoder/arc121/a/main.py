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
    xy = [LI() for _ in range(N)]
    xy_s = []
    xy_s.append(list(sorted(enumerate(xy), key=lambda x: x[1][0])))
    xy_s.append(list(sorted(enumerate(xy), key=lambda x: x[1][1])))
    # print(xy_s[0])
    # print(xy_s[1])

    top6 = []
    for i in range(2):
        top6.append(((xy_s[i][0][0], xy_s[i][-1][0]), xy_s[i][-1][1][i] - xy_s[i][0][1][i]))
        top6.append(((xy_s[i][0][0], xy_s[i][-2][0]), xy_s[i][-2][1][i] - xy_s[i][0][1][i]))
        top6.append(((xy_s[i][1][0], xy_s[i][-1][0]), xy_s[i][-1][1][i] - xy_s[i][1][1][i]))
    top6.sort(key=lambda x: x[1], reverse=True)
    # print(top6)
    if top6[0][0] == top6[1][0]:
        print(top6[2][1])
    else:
        print(top6[1][1])

if __name__ == '__main__':
    resolve()
