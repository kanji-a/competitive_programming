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
    A = LI()

    # lから奇数番目の和と偶数番目の和が等しいことが0にできる必要十分条件
    acm = [0]
    d = collections.defaultdict(list)
    for i in range(N):
        if i % 2 == 0:
            acm.append(acm[-1] + A[i])
        else:
            acm.append(acm[-1] - A[i])
        d[acm[-1]].append(i)
    print(acm)
    print(d)
    ans = 0
    for i in range(N):
        s = acm[i+1]
        idx = bisect.bisect_left(d[s], i + 1)
        print(idx)
        ans += len(d[s]) - idx
        print('ans', ans)

    print(ans)

if __name__ == '__main__':
    resolve()
